from django.db import models

# Create your models here.

class Categoria(models.Model):
    descripcion=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.descripcion

class Articulo(models.Model):
    titulo = models.CharField(max_length=200, null=True)
    # fragmento=models.CharField(max_length=100)
    contenido=models.TextField()
    categoria=models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return self.titulo
