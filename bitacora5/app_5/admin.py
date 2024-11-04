from django.contrib import admin
from .models.models_categoria import Categoria
from .models.models_distribuidora import Distribuidora
from .models.models_factura import Factura
from .models.models_negocio import Negocio
from .models.models_producto import Producto
from .models.models_usuario import Caja, Usuario

# Register your models here.
class AdminCategoria(admin.ModelAdmin):
    list_display = ['categoria_nombre']

admin.site.register(Categoria, AdminCategoria)

class AdminDistribuidor(admin.ModelAdmin):
    list_display = ['nombre_distribuidor','rut_distribuidor']

admin.site.register(Distribuidora, AdminDistribuidor)

class AdminFactura(admin.ModelAdmin):
    list_display = ['fecha_factura','forma_pago','iva','impuesto_iva','bebidas','impuesto_bebidas','otros','impuesto_otros','negocio_id','distribuidor_id','item_id','caja_id']

admin.site.register(Factura, AdminFactura)

class AdminNegocio(admin.ModelAdmin):
    list_display = ['persona_responsable','rut_persona_responsable','rut_negocio']

admin.site.register(Negocio, AdminNegocio)

class AdminProducto(admin.ModelAdmin):
    list_display = ['code','nombre_item','tipo_item','valor_unidad','valor_kilo','cantidad_item','fecha_elaboracion','fecha_vencimiento','categoria_id','stock','qr_code']

admin.site.register(Producto, AdminProducto)

class AdminUsuario(admin.ModelAdmin):
    list_display = ['nombre','rol','password']

admin.site.register(Usuario, AdminUsuario)

class AdminCaja(admin.ModelAdmin):
    list_display = ['nombre','rol','password','tiempo_inicio','tiempo_fin']

admin.site.register(Caja, AdminCaja)