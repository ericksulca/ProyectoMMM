from django.db import models
from apps.usuario.models import Usuario

# Create your models here.
class Testimonio(models.Model):
    contenido = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    fecha_registro=models.DateField(auto_now_add=True, null=True)
    fecha_modificacion=models.DateField(auto_now=True, null=True)
