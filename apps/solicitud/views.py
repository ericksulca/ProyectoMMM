from django.core import serializers
from django.http import JsonResponse
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# import json

from .forms import NuevaSolicitudForm
from apps.usuario.models import Usuario
from apps.solicitud.models import Solicitud
from apps.usuario.views import notificaciones_usuario
from apps.usuario.views import cantidad_notificaciones
# Create your views here.

def index_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)

    context = {
        'usuario': oUsuario,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
    }

    return render(request, 'solicitud/index.html', context)

def editar_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)

    context = {
        'usuario': oUsuario,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
    }

    return render(request, 'solicitud/editar.html', context)


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def nueva_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    if request.method == 'POST':
        form = NuevaSolicitudForm(request.POST)
        monto_faltante = request.POST['monto']
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = oUsuario
            solicitud.monto_faltante = monto_faltante
            solicitud.save()
            # mensaje={'success':'success'}
            # return JsonResponse(mensaje)
            # data = serializers.serialize(
            #             'json',
            #             mensaje
            #         )
            #
            # return HttpResponse(data, content_type='application/json')
            messages.add_message(request, messages.INFO, "Su solicitud fue agergada a la lista de espera con éxito. Recibira una notificación al recibir el depósito.")
            return redirect('solicitud:nueva_solicitud')
        else:
            messages.add_message(request, messages.INFO, "Ocurrio un error en el procesamiento de la solicutud, por favor inténtelo neuvamente.")
            return redirect('solicitud:nueva_solicitud')
    else:
        form = NuevaSolicitudForm()

    context = {
        'usuario': oUsuario,
        'form': form,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
    }

    return render(request, 'solicitud/nueva.html', context)


# Función que da como respuesta monto de las solicitudes de prestamo activas
def total_monto_solicitudes():
    monto_prestamo = Solicitud.objects.filter(estado=True, pagado=False).aggregate(Sum('monto_faltante'))
    # monto_prestamo=Solicitud.objects.filter(estado=True,pagado=False)[:1]
    # monto_prestamo = Solicitud.objects.filter(estado=True, pagado=False,monto_faltante__gt=0)[:1].get()
    return monto_prestamo['monto_faltante__sum']
    # return monto_prestamo['monto_faltante']
