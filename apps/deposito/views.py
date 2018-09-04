from django.db.models import Q
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

from apps.solicitud.views import total_monto_solicitudes
from apps.usuario.models import Usuario
from .models import Operacion
# Create your views here.

def index(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    monto = total_monto_solicitudes()
    context = {
        'usuario': oUsuario,
        'monto': monto
    }

    return render(request, 'deposito/index.html', context)



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