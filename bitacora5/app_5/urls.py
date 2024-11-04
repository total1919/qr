from django.urls import path
from . import views

urlpatterns =[
    path('qr_codes/<str:nombre_item>_<str:code>_<int:precio>/', views.mostrar_qr, name='mostrar_qr'), 
]