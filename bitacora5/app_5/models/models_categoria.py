from django.db import models
from .choices import CATEGORIA

class Categoria(models.Model):
    categoria_nombre = models.CharField(
        max_length=12,
        choices=CATEGORIA,
        default='Utilidad'
    )

