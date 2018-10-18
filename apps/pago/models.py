from django.db import models

from apps.deposito.models import Operacion

# from apps.usuario.models import Usuario
# from apps.solicitud.models import Solicitud

# Create your models here.


class General(models.Model):

    operacion = models.ForeignKey(Operacion, on_delete=models.PROTECT)
    # monto_solicitado=models.IntegerField()
    tasa_interes=models.DecimalField(max_digits=10, decimal_places=2)
    monto_actual=models.DecimalField(max_digits=10, decimal_places=2)
    fecha_actual = models.DateTimeField(auto_now=True)
