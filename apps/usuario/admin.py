from django.contrib import admin

from .models import Entidad_bancaria, Usuario

# Register your models here.

admin.site.register(Entidad_bancaria)
admin.site.register(Usuario)