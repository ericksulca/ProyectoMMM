from django.db import models

# Create your models here.
class General(models.Model):
    inscripcion=models.IntegerField()
    enlace_youtube=models.CharField(max_length=600)
