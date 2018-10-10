from django.db import models

from apps.usuario.models import Usuario
from apps.solicitud.models import  Solicitud

# Create your models here.

class Operacion(models.Model):
    TIPO_MOVIMIENTO = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
    )

    monto = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_final = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now=True)
    estado = models.IntegerField(default=1)
    tipo_movimiento = models.CharField(max_length=10, choices=TIPO_MOVIMIENTO)

    usuario_emisor = models.ForeignKey(
        Usuario, related_name='UsuarioEmisor',
        on_delete=models.PROTECT
    )
    usuario_receptor = models.ForeignKey(
        Usuario, related_name='UsuarioReceptor',
        on_delete=models.PROTECT
    )
    solicitud = models.ForeignKey(
        Solicitud,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return '%s %s %s' % (self.usuario_emisor, self.movimiento, self.monto)

    @property
    def movimiento(self):
        return self.tipo_movimiento


class Operacion_backup(models.Model):
    TIPO_MOVIMIENTO = (
        ('retiro', 'Retiro'),
        ('deposito', 'Depósito'),
    )

    monto_backup = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_backup = models.DateTimeField(auto_now=True)
    estado_backup = models.IntegerField(default=1)
    tipo_movimiento_backup = models.CharField(max_length=8, choices=TIPO_MOVIMIENTO)

    usuario_emisor_backup = models.ForeignKey(
        Usuario, related_name='UsuarioEmisorBackup',
        on_delete=models.PROTECT
    )
    usuario_receptor_backup = models.ForeignKey(
        Usuario, related_name='UsuarioReceptorBackup',
        on_delete=models.PROTECT
    )
    solicitud_backup = models.ForeignKey(
        Solicitud,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return '%s %s %s' % (self.usuario_emisor_backup, self.movimiento_backup, self.monto_backup)

    @property
    def movimiento_backup(self):
        return self.tipo_movimiento_backup
