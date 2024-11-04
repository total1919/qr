from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models.models_producto import Producto

def mostrar_qr(request, nombre_item, code, precio):
    # Obtén el objeto que contiene el código QR usando el nombre del ítem
    qr_item = get_object_or_404(Producto, nombre_item=nombre_item, )

    # Si necesitas pasar información adicional a la plantilla
    context = {
        'qr_item': qr_item,
    }
    
    return render(request, 'app_5/mostrar_qr.html', context)

# Create your views here.
