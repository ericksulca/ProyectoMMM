from django.db import models

from apps.usuario.models import Usuario

# Create your models here.

class Solicitud(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    confirmacion = models.BooleanField(default=False)
    pagado = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.usuario, self.monto)