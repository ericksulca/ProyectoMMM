from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Entidad_bancaria(models.Model):
    nombre = models.CharField(max_length=50)
    logo = models.ImageField(blank=True, upload_to='entidades_bancarias')

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    dni = models.IntegerField(
        primary_key=True,
        validators=[MinValueValidator(10000000), 
        MaxValueValidator(99999999)],
        )
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    foto_perfil = models.ImageField(blank=True, upload_to='usuario')
    numero_cuenta = models.IntegerField(unique=True)
    saldo = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, default=0
        )

    usuario_login = models.OneToOneField(User, on_delete=models.PROTECT)    
    entidad_bancaria = models.ForeignKey(Entidad_bancaria, on_delete=models.PROTECT)
    dni_referido = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    
    def __str__(self):
        return self.nombres
    
    @property
    def nombre_completo(self):
        return '%s %s %s' % (self.nombres, self.apellido_paterno, self.apellido_materno)
