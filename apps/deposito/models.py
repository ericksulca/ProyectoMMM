from django.db import models

from apps.usuario.models import Usuario
from apps.solicitud.models import  Solicitud

# # Create your models here.

class Operaciones(models.Model):
    TIPO_MOVIMIENTO = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
    )

    monto = models.DecimalField(max_digits=10, decimal_places=2) # Quizas? este monto es el mismo en solicitud
    fecha = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    tipo_movimiento = models.CharField(max_length=8, choices=TIPO_MOVIMIENTO)

    usuario_asignado = models.ForeignKey(
        Usuario, related_name='UsuarioAsignado',
        blank=True,
        null=True,
        on_delete=models.PROTECT
        )
    usuario = models.ForeignKey(
        Usuario, related_name='UsuarioPaga',
        on_delete=models.PROTECT
        )
    solicitud = models.ForeignKey(
        Solicitud,
        blank=True,
        null=True,
        on_delete=models.PROTECT
        )
    
    def __str__(self):
        return self.usuario + self.tipo_movimiento + self.monto
    
    def movimiento(self):
        return self.tipo_movimiento


class OperacionesBackUp(models.Model):
    TIPO_MOVIMIENTO = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
    )

    monto_backup = models.DecimalField(max_digits=10, decimal_places=2) # Quizas? este monto es el mismo en solicitud
    fecha_backup = models.DateTimeField(auto_now=True)
    estado_backup = models.BooleanField(default=True)
    tipo_movimiento_backup = models.CharField(max_length=8, choices=TIPO_MOVIMIENTO)

    usuario_asignado_backup = models.ForeignKey(
        Usuario, related_name='UsuarioAsignadoBackUp',
        blank=True,
        null=True,
        on_delete=models.PROTECT
        )
    usuario_backup = models.ForeignKey(
        Usuario, related_name='UsuarioPagaBackUp',
        on_delete=models.PROTECT
        )
    solicitud_backup = models.ForeignKey(
        Solicitud,
        blank=True,
        null=True,
        on_delete=models.PROTECT
        )
    
    def __str__(self):
        return self.usuario_backup + self.tipo_movimiento_backup + self.monto_backup
    
    def movimiento(self):
        return self.tipo_movimiento_backup