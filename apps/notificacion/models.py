from django.db import models
from apps.usuario.models import Usuario

# Create your models here.
class Notificacion(models.Model):

    id_emisor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    id_receptor = models.IntegerField()
    estado = models.IntegerField()
    fecha_registro=models.DateTimeField(auto_now_add=True, null=True)
    tipo=models.CharField(max_length=100)
    monto=models.IntegerField()
    confirmado=models.IntegerField()

class Notificacion_depositar(models.Model):

    receptor = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    emisor = models.IntegerField()
    estado = models.IntegerField()
    fecha_registro=models.DateTimeField(auto_now_add=True, null=True)
    tipo=models.CharField(max_length=100)
    monto=models.IntegerField()
    confirmado=models.IntegerField()
