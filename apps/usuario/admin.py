from django.contrib import admin

from .models import Entidad_bancaria, Usuario, Mensaje, Mensaje_Usuario

# Register your models here.

admin.site.register(Entidad_bancaria)
admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Mensaje_Usuario)