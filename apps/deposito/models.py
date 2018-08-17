from django.db import models

from apps.usuario.models import Usuario
from apps.solicitud.models import  Solicitud

# Create your models here.

# Alternativa es modificar el modelo PAGO a 'movimiento' y agregar columna 'tipo de operacion'
class Deposito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    solicitud = models.ForeignKey(Solicitud, on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=10, decimal_places=2) # Mismo que en solicitud
    fecha = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario + self.monto
