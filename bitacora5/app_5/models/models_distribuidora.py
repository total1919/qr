from django.db import models

class Distribuidora(models.Model):
    nombre_distribuidor = models.CharField(max_length=50, unique=True)
    rut_distribuidor = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre_distribuidor

