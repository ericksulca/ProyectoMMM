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
from apps.usuario.views import plazo_horas
from apps.usuario.views import cantidad_notificaciones
from apps.pago.models import Pago
# Create your views here.

def index_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)

    context = {
        'usuario': oUsuario,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'horas':plazo_horas(request),
    }

    return render(request, 'solicitud/index.html', context)

def editar_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)

    context = {
        'usuario': oUsuario,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'horas':plazo_horas(request),
    }

    return render(request, 'solicitud/editar.html', context)


from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, date, time, timedelta
import calendar
from django.utils import timezone
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
            messages.add_message(request, messages.INFO, "Su solicitud fue agregada a la lista de espera con éxito. Recibira una notificación al recibir el depósito.")
            return redirect('solicitud:nueva_solicitud')
        else:
            messages.add_message(request, messages.INFO, "Ocurrio un error en el procesamiento de la solicutud, por favor inténtelo neuvamente.")
            return redirect('solicitud:nueva_solicitud')
    else:
        form = NuevaSolicitudForm()


    oPago=Pago.objects.filter(usuario_id=oUsuario, confirmado=0)

    if request.user.is_staff:
        oPago=''


    now = timezone.now()
    fecha_usuario = oUsuario.fecha
    resultado = now - fecha_usuario
    dias_restantes=30-resultado.days
    form_habilitado=False
    # print(resultado.days)
    if resultado.days > 29:
        form_habilitado=True
    # else:
    #     print ("Menor")

    context = {
        'usuario': oUsuario,
        'form': form,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'horas':plazo_horas(request),
        'form_habilitado':form_habilitado,
        'fecha_registro':fecha_usuario,
        'dias_restantes':dias_restantes,
        'pago':oPago,
    }



    return render(request, 'solicitud/nueva.html', context)


# Función que da como respuesta monto de las solicitudes de prestamo activas
def total_monto_solicitudes():
    monto_prestamo = Solicitud.objects.filter(estado=True, pagado=False).aggregate(Sum('monto_faltante'))
    # monto_prestamo=Solicitud.objects.filter(estado=True,pagado=False)[:1]
    # monto_prestamo = Solicitud.objects.filter(estado=True, pagado=False,monto_faltante__gt=0)[:1].get()
    return monto_prestamo['monto_faltante__sum']
    # return monto_prestamo['monto_faltante']
