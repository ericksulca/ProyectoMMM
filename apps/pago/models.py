from django.db import models

from apps.deposito.models import Operacion
from apps.usuario.models import Usuario


# from apps.usuario.models import Usuario
# from apps.solicitud.models import Solicitud

# Create your models here.


class Pago(models.Model):

    operacion = models.ForeignKey(Operacion, on_delete=models.PROTECT)
    # monto_solicitado=models.IntegerField()
    tasa_interes=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    tasa_interes_referente=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    monto_solicitado=models.DecimalField(max_digits=10,decimal_places=2,null=True)
    monto_actual=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    fecha_actual = models.DateField(auto_now=True,null=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT, null=True)
    confirmado=models.IntegerField()
    confirmado_referente=models.IntegerField()
    ganancia_referente=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    ganancia_referido=models.DecimalField(max_digits=10, decimal_places=2,null=True)
    # referente_beneficiado = models.IntegerField()
