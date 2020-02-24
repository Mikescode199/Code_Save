from django.db import models

# Create your models here.

class Codigo(models.Model):
    tipo_codigo = models.CharField(max_length=30)
    nombre_etiqueta = models.CharField(max_length=30)
    codigo_guardado = models.TextField()

