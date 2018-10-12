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
    fecha = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    foto_perfil = models.ImageField(blank=True, upload_to='usuario', default='usuario/Koala.jpg')
    numero_cuenta = models.CharField(max_length=100,unique=True)
    activo = models.BooleanField(default=True)

    usuario_login = models.OneToOneField(User, on_delete=models.PROTECT)
    entidad_bancaria = models.ForeignKey(Entidad_bancaria, on_delete=models.PROTECT)
    dni_referido = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True)
    depositos_pendientes=models.IntegerField(default=1,null=True)

    def __str__(self):
        return self.nombres

    @property
    def nombre_completo(self):
        return '%s %s %s' % (self.nombres, self.apellido_paterno, self.apellido_materno)


class Saldo(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    saldo = models.DecimalField(
        max_digits=10, decimal_places=2,
        blank=True, default=0
        )

    usuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)

    def __str__(self):
        return 'El saldo es de %s en la fecha %s' % (self.saldo, self.fecha_creacion)


class Mensaje(models.Model):
    asunto = models.CharField(max_length=50)
    fecha_redaccion = models.DateTimeField(auto_now_add=True)
    texto_mensaje = models.TextField()

    emisor = models.ForeignKey(
        Usuario,
        related_name='emisor',
        on_delete=models.PROTECT
        )


class Mensaje_Usuario(models.Model):
    leido = models.BooleanField(default=True)

    receptor = models.ForeignKey(
        Usuario,
        related_name='receptor',
        on_delete=models.PROTECT
        )
    mensaje = models.ForeignKey(
        Mensaje,
        on_delete=models.PROTECT
        )
