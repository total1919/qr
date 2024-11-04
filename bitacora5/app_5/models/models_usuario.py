from django.db import models
from .choices import ROL_USUARIO

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    rol = models.CharField(max_length=20, choices=ROL_USUARIO)
    password = models.CharField(max_length=10, unique=True)

class Caja(Usuario):
    tiempo_inicio = models.DateTimeField(auto_now_add=True)  # Registra el inicio de conexión
    tiempo_fin = models.DateTimeField(null=True, blank=True)  # Registra la desconexión

    def tiempo_conexion_total(self):
        if self.tiempo_fin:
            return self.tiempo_fin - self.tiempo_inicio
        return None


