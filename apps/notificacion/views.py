from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse


from apps.notificacion.models import Notificacion


# Create your views here.


def leer(request,id):
    oNotificacion=Notificacion.objects.get(id=id)

    oNotificacion.estado=1
    oNotificacion.save()
    return HttpResponse(str("s"))
