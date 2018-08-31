from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=200)
    fragmento=models.CharField(max_length=100)
    contenido=models.CharField(max_length=2000)
    tipo=models.CharField(max_length=10)
