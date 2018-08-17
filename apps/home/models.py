from django.db import models

# Create your models here.
class Banner(models.Model):
    titulo = models.CharField(max_length=100)
    banner = models.ImageField(blank=True, upload_to='banner')

    def __str__(self):
        return self.titulo
