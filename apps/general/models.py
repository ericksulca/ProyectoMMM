from django.db import models

# Create your models here.
class General(models.Model):
    inscripcion=models.IntegerField()
    monto_minimo=models.IntegerField()
    enlace_youtube=models.CharField(max_length=600)
    horas_plazo_deposito=models.IntegerField()


class Tarifa(models.Model):
    nombre=models.CharField(max_length=50)
    tasa_interes=models.IntegerField()
