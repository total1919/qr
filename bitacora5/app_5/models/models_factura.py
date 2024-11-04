from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from .choices import FORMA_PAGO

from .models_negocio import Negocio
from .models_producto import Item
from .models_distribuidora import Distribuidora
from .models_usuario import Caja

def validate_iva(value):
        if value != 19:
            raise ValidationError("El IVA debe ser del 19%.")

class Detalle_Factura(models.Model):
    fecha_factura = models.DateTimeField(auto_now_add=True)
    forma_pago = models.CharField(
         max_length=8,
         choices= FORMA_PAGO,
         default='efectivo'
    )
    iva = models.BooleanField(default=True, editable=False)
    impuesto_iva = models.DecimalField(
        max_digits=4, 
        decimal_places=2, 
        default=(19), 
        validators=[validate_iva], 
        editable=False
    )
    bebidas = models.BooleanField(default=False)
    impuesto_bebidas = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])
    otros = models.BooleanField(default=False)
    impuesto_otros = models.FloatField(null=True, blank=True, validators=[MinValueValidator(0.0)])

class Factura(Detalle_Factura):
    negocio_id = models.ForeignKey(
        Negocio,
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='negocio_factura'
    )
    distribuidor_id = models.ForeignKey(
        Distribuidora,
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='distribuidora_factura'
    )
    item_id = models.ForeignKey(
        Item,
        on_delete=models.DO_NOTHING,
        null=False,
        related_name='producto_factura'
    )
    caja_id = models.ForeignKey(
         Caja,
         on_delete=models.DO_NOTHING,
         null=False,
         related_name='caja_factura'
    )
