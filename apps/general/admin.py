from django.contrib import admin

from .models import General
from .models import Tarifa
# Register your models here.

admin.site.register(General)

admin.site.register(Tarifa)
