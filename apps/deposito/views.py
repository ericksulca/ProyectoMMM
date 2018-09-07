from decimal import Decimal

from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.solicitud.views import total_monto_solicitudes
from apps.usuario.models import Usuario
from apps.solicitud.models import Solicitud
from .models import Operacion
from .forms import  NuevoDeposito
# Create your views here.

def index(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    monto = total_monto_solicitudes()
    context = {
        'usuario': oUsuario,
        'monto': monto
    }

    return render(request, 'deposito/index.html', context)


def deposito_usuario(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    if request.method == 'POST':
        form = NuevoDeposito(request.POST)
        if form.is_valid():
            operacion = form.save(commit=False)
            operacion.tipo_movimiento = 'deposito'
            operacion.save()
            return redirect('deposito:index')
        else:
            return redirect('deposito:index')
    else:
        form = NuevoDeposito()
    
    context = {
        'usuario': oUsuario,
        'form': form
    }

    return render(request, 'deposito/nueva.html', context)


def deposito_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oSolicitudes = Solicitud.objects.filter(pagado=False, estado=True).order_by('-fecha')
    if request.method == 'POST':
        monto_total = Decimal(request.POST['monto'])
        for solicitud in oSolicitudes:
            if monto_total >= solicitud.monto_faltante:
                ultima_operacion = Operacion.objects.latest(field_name='fecha')
                saldo_final_anterior = ultima_operacion.saldo_final
                monto_operacion = solicitud.monto_faltante
                Saldo_final_operacion = ultima_operacion.saldo_final + monto_operacion
                monto_total -= solicitud.monto_faltante
                solicitud.monto_completado = solicitud.monto
                solicitud.monto_faltante = 0
                solicitud.pagado = True
                solicitud.save()
                operacion = Operacion(
                    monto = monto_operacion,
                    saldo_inicial = saldo_final_anterior,
                    saldo_final = Saldo_final_operacion,
                    tipo_movimiento = 'deposito',
                    usuario_emisor = oUsuario,
                    usuario_receptor = solicitud.usuario,
                    solicitud = solicitud
                )
                operacion.save()
            else:
                ultima_operacion = Operacion.objects.latest(field_name='fecha')
                saldo_final_anterior = ultima_operacion.saldo_final
                monto_operacion = solicitud.monto_faltante
                Saldo_final_operacion = ultima_operacion.saldo_final + monto_operacion
                solicitud.monto_completado += monto_total 
                solicitud.monto_faltante -= monto_total 
                solicitud.save()
                operacion = Operacion(
                    monto = monto_operacion,
                    saldo_inicial = saldo_final_anterior,
                    saldo_final = Saldo_final_operacion,
                    tipo_movimiento = 'deposito',
                    usuario_emisor = oUsuario,
                    usuario_receptor = solicitud.usuario,
                    solicitud = solicitud
                )
                operacion.save()
                break
    context = {
        'usuario': oUsuario
    }

    return render(request, 'deposito/deposito_solicitud.html', context)



def operaciones_usuario(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oOperaciones = Operacion.objects.filter(Q(usuario_emisor=oUsuario) | Q(usuario_receptor=oUsuario)).order_by('-fecha').only('monto', 'fecha', 'tipo_movimiento', 'usuario_emisor', 'saldo_inicial', 'saldo_final')
    data = serializers.serialize(
        'json',
        oOperaciones,
        fields = ['monto', 'fecha', 'tipo_movimiento', 'usuario_emisor', 'saldo_inicial', 'saldo_final']
    )
    return HttpResponse(data, content_type='application/json')



def operaciones_usuario_chart(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oOperaciones = Operacion.objects.filter(Q(usuario_emisor=oUsuario) | Q(usuario_receptor=oUsuario)).order_by('fecha').only('fecha', 'saldo_final')[:10]
    data = serializers.serialize(
        'json',
        oOperaciones,
        fields = ['fecha', 'saldo_final']
    )
    return HttpResponse(data, content_type='application/json')