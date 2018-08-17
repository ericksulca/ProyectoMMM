from django.db import models

from apps.usuario.models import Usuario

# Create your models here.

class Pago(models.Model):
    usuario_asignado = models.ForeignKey(Usuario, related_name='UsuarioAsignado',on_delete=models.PROTECT)
    usuario = models.ForeignKey(Usuario, related_name='UsuarioPaga',on_delete=models.PROTECT)
    monto = models.DecimalField(max_digits=10, decimal_places=2) # Quizas? este monto es el mismo en solicitud
    fecha = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.usuario + self.usuario_asignado + self.monto