from django.db import models

class Negocio(models.Model):
    persona_responsable = models.CharField(max_length=50, unique=True, null=False)
    rut_persona_responsable = models.CharField(max_length=10, unique=True, null=False)
    rut_negocio = models.CharField(max_length=10, unique=True, null=False)
    