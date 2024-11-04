from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from .models_categoria import Categoria

from .choices import UNIDAD_O_KILO

import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Item(models.Model):
    code = models.CharField(max_length=12, unique=True)
    nombre_item = models.CharField(max_length=100)
    tipo_item = models.CharField(
        max_length=6,
        choices=UNIDAD_O_KILO,
        default='unidad'
    )
    valor_unidad = models.IntegerField(
        validators=[MinValueValidator(0)],
        null=True,
        blank=True
    )
    valor_kilo = models.FloatField(
        validators=[MinValueValidator(0.0)],
        null=True,
        blank=True
    )
    cantidad_item = models.FloatField(
        validators=[MinValueValidator(0.0)],
        null=True,
        blank=True
    )
    fecha_elaboracion = models.DateField()
    fecha_vencimiento = models.DateField()

    class Meta:
        unique_together = ['nombre_item','code']

    def __str__(self):
        return f'{self.nombre_item} - {self.code}'

    def clean(self):
        if self.fecha_vencimiento < self.fecha_elaboracion:
            raise ValidationError("fecha de vencimiento inválida")
    
    def precio(self):
    # Utiliza `valor_unidad` o `valor_kilo` según cuál esté disponible
        valor = self.valor_unidad or self.valor_kilo
        if valor:
            precio = valor * 1.19 * 1.3  # Aplicamos el 19% de impuesto y el 30% de margen
            return precio
        return None
        

class Producto(Item):
    categoria_id = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        null=True,
        related_name='categoria_producto'
    )
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    qr_code = models.ImageField(upload_to='qr_codes', blank=True, unique=True)
    
    def save(self, *args, **kwargs):
        try:
            # Generar el código QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(self.nombre_item)
            qr.make(fit=True)

            # Crear imagen del código QR
            qrcode_img = qr.make_image(fill="black", back_color="white").convert('RGB')

            # Crear un lienzo blanco del mismo tamaño que el QR
            canvas_size = qrcode_img.size
            canvas = Image.new('RGB', canvas_size, 'white')
            canvas.paste(qrcode_img)

            self.precio()

            # Guardar la imagen en un buffer
            const = f'qr_code_{self.nombre_item}_{self.code}_{self.precio}.png'
            buffer = BytesIO()
            canvas.save(buffer, format='PNG')
            buffer.seek(0)

            # Guardar la imagen en el campo qr_code
            self.qr_code.save(const, File(buffer), save=False)

            # Cerrar el canvas y liberar el buffer
            canvas.close()
            buffer.close()

        except Exception as e:
            print("Error al generar el código QR:", e)
        
        # Guardar la instancia del modelo
        super().save(*args, **kwargs)
