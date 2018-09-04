from django.db import models
from django.db.models import Sum

from apps.usuario.models import Usuario

# Create your models here.

class Solicitud(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, blank=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    monto_completado = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    monto_faltante = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    confirmacion = models.BooleanField(default=False)
    pagado = models.BooleanField(default=False)
    estado = models.BooleanField(default=True)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return '%s %s' % (self.usuario, self.monto)


    # Función que da como respuesta monto de las solicitudes de prestamo activas
    def total_monto_solicitudes(self):
        monto_prestamo = Solicitud.objects.filter(estado=True, pagado=False).aggregate(Sum('monto_faltante'))
        return monto_prestamo['monto__sum']