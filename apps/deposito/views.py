from decimal import Decimal

from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect

from apps.solicitud.views import total_monto_solicitudes
from apps.usuario.views import notificaciones_usuario
from apps.usuario.views import cantidad_notificaciones
from apps.usuario.models import Usuario
from apps.notificacion.models import Notificacion
from apps.notificacion.models import Notificacion_depositar
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
    oSolicitudes = Solicitud.objects.filter(pagado=False, estado=True).order_by('fecha')
    lista_receptores=[]
    monto_depositar=[]
    notificacion=''
    # oNotificaciones=Notificacion.objects.filter(id_emisor_id=oUsuario.dni).order_by('-id')
    # oNotificaciones=Notificacion.objects.all()
    if request.method == 'POST':
        monto_total = Decimal(request.POST['monto'])
        for solicitud in oSolicitudes:

            if monto_total >= solicitud.monto_faltante:

                monto_depositar.append(monto_total-(monto_total-solicitud.monto_faltante))


                ultima_operacion_emisor = Operacion.objects.filter(usuario_receptor=oUsuario).latest(field_name='fecha')
                ultima_operacion_receptor = Operacion.objects.filter(usuario_receptor=solicitud.usuario).latest(field_name='fecha')

                #REGISTRAR NOTIFICACION PARA ENVIAR AL RECEPTOR
                notificacion=Notificacion(
                    id_emisor_id=oUsuario.dni,
                    id_receptor=ultima_operacion_receptor.usuario_receptor_id,
                    usuario_sesion=ultima_operacion_receptor.usuario_receptor_id,
                    tipo='deposito_realizado_receptor',
                    estado=0,
                    monto=monto_total-(monto_total-solicitud.monto_faltante),
                    confirmado=0
                )
                notificacion.save()
                #REGISTRAR NOTIFICACION PARA ENVIAR AL EMISOR
                notificacion=Notificacion(
                    id_emisor_id=ultima_operacion_receptor.usuario_receptor_id,
                    id_receptor=oUsuario.dni,
                    usuario_sesion=oUsuario.dni,
                    tipo='deposito_realizado_emisor',
                    estado=0,
                    monto=monto_total-(monto_total-solicitud.monto_faltante),
                    confirmado=0
                )
                notificacion.save()
                # notificacion_depositar=Notificacion_depositar(
                #     emisor=oUsuario.dni,
                #     receptor_id=ultima_operacion_receptor.usuario_receptor_id,
                #     tipo='deposito',
                #     estado=0,
                #     monto=monto_total-(monto_total-solicitud.monto_faltante),
                #     confirmado=0
                # )
                # notificacion_depositar.save()
                saldo_final_anterior_emisor = ultima_operacion_emisor.saldo_final
                saldo_final_anterior_receptor = ultima_operacion_receptor.saldo_final
                monto_operacion = solicitud.monto_faltante
                Saldo_final_operacion_emisor = ultima_operacion_emisor.saldo_final - monto_operacion
                Saldo_final_operacion_receptor = ultima_operacion_receptor.saldo_final + monto_operacion
                monto_total -= solicitud.monto_faltante
                solicitud.monto_completado = solicitud.monto
                solicitud.monto_faltante = 0
                solicitud.pagado = True
                solicitud.save()
                operacion = Operacion(
                    monto = monto_operacion,
                    saldo_inicial = saldo_final_anterior_emisor,
                    saldo_final = Saldo_final_operacion_emisor,
                    tipo_movimiento = 'retiro',
                    usuario_emisor = oUsuario,
                    usuario_receptor = oUsuario,
                    solicitud = solicitud
                )
                operacion.save()

                operacion = Operacion(
                    monto = monto_operacion,
                    saldo_inicial = saldo_final_anterior_receptor,
                    saldo_final = Saldo_final_operacion_receptor,
                    tipo_movimiento = 'deposito',
                    usuario_emisor = oUsuario,
                    usuario_receptor = solicitud.usuario,
                    solicitud = solicitud
                )
                operacion.save()
                lista_receptores.append(ultima_operacion_receptor.usuario_receptor_id)



            else:
                monto_depositar.append(monto_total)


                ultima_operacion_emisor = Operacion.objects.filter(usuario_receptor=oUsuario).latest(field_name='fecha')
                ultima_operacion_receptor = Operacion.objects.filter(usuario_receptor=solicitud.usuario).latest(field_name='fecha')
                #REGISTRAR NOTIFICACION PARA ENVIAR AL RECEPTOR
                notificacion=Notificacion(
                    id_emisor_id=oUsuario.dni,
                    id_receptor=ultima_operacion_receptor.usuario_receptor_id,
                    usuario_sesion=ultima_operacion_receptor.usuario_receptor_id,
                    tipo='deposito_realizado_receptor',
                    estado=0,
                    monto=monto_total,
                    confirmado=0
                )
                notificacion.save()
                #REGISTRAR NOTIFICACION PARA ENVIAR AL EMISOR
                notificacion=Notificacion(
                    id_emisor_id=ultima_operacion_receptor.usuario_receptor_id,
                    id_receptor=oUsuario.dni,
                    usuario_sesion=oUsuario.dni,
                    tipo='deposito_realizado_emisor',
                    estado=0,
                    monto=monto_total,
                    confirmado=0
                )
                notificacion.save()
                # notificacion_depositar=Notificacion_depositar(
                #     emisor=oUsuario.dni,
                #     receptor_id=ultima_operacion_receptor.usuario_receptor_id,
                #     tipo='deposito',
                #     estado=0,
                #     monto=monto_total,
                #     confirmado=0
                # )
                # notificacion_depositar.save()
                saldo_final_anterior_emisor = ultima_operacion_emisor.saldo_final
                saldo_final_anterior_receptor = ultima_operacion_receptor.saldo_final
                monto_operacion = solicitud.monto_faltante
                Saldo_final_operacion_emisor = ultima_operacion_emisor.saldo_final - monto_operacion
                Saldo_final_operacion_receptor = ultima_operacion_receptor.saldo_final + monto_operacion
                solicitud.monto_completado += monto_total
                solicitud.monto_faltante -= monto_total
                solicitud.save()
                operacion = Operacion(
                    monto = monto_operacion,
                    saldo_inicial = saldo_final_anterior_emisor,
                    saldo_final = Saldo_final_operacion_emisor,
                    tipo_movimiento = 'retiro',
                    usuario_emisor = oUsuario,
                    usuario_receptor = oUsuario,
                    solicitud = solicitud
                )
                operacion.save()

                operacion = Operacion(
                    monto = monto_operacion,
                    saldo_inicial = saldo_final_anterior_receptor,
                    saldo_final = Saldo_final_operacion_receptor,
                    tipo_movimiento = 'deposito',
                    usuario_emisor = oUsuario,
                    usuario_receptor = solicitud.usuario,
                    solicitud = solicitud
                )
                operacion.save()
                lista_receptores.append(ultima_operacion_receptor.usuario_receptor_id)


                break

    monto = total_monto_solicitudes()
    deposito_realizar=Notificacion.objects.filter(usuario_sesion=oUsuario.dni, confirmado=0,tipo="deposito_realizado_emisor")
    context = {
        'usuario': oUsuario,
        'lista_receptores':lista_receptores,
        # 'monto_depositar':monto_depositar,
        'monto': monto,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'deposito_realizar':deposito_realizar
    }

    return render(request, 'deposito/deposito_solicitud.html', context)



def operaciones_usuario(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oOperaciones = Operacion.objects.filter(usuario_receptor=oUsuario).only('monto', 'fecha', 'tipo_movimiento', 'usuario_emisor', 'saldo_inicial', 'saldo_final').order_by('-fecha')
    data = serializers.serialize(
        'json',
        oOperaciones,
        fields = ['monto', 'fecha', 'tipo_movimiento', 'usuario_emisor', 'saldo_inicial', 'saldo_final']
    )
    return HttpResponse(data, content_type='application/json')

def operaciones_usuario_chart(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oOperaciones = Operacion.objects.filter(usuario_receptor=oUsuario).order_by('fecha').only('fecha', 'saldo_final')[:10]
    data = serializers.serialize(
        'json',
        oOperaciones,
        fields = ['fecha', 'saldo_final']
    )
    return HttpResponse(data, content_type='application/json')

def confirmar_deposito(request,id,dni_receptor):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oNotificacionDepositar=Notificacion.objects.get(id=id)
    oNotificacionDepositar.confirmado=1
    oNotificacionDepositar.save()

    notificacion=Notificacion(
        id_emisor_id=oUsuario.dni,
        id_receptor=dni_receptor,
        tipo='deposito_confirmado_receptor',
        usuario_sesion=dni_receptor,
        estado=0,
        monto=oNotificacionDepositar.monto,
        confirmado=0
    )
    notificacion.save()

    return HttpResponse(str("s"))
