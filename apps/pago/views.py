from django.shortcuts import render


from apps.usuario.views import plazo_horas
from apps.usuario.views import cantidad_notificaciones
from apps.pago.models import Pago
from apps.usuario.views import notificaciones_usuario
from apps.usuario.models import Usuario
# Create your views here.

def confirmar_pago(request):
    context = {"titulo": "Confirmar Pago"}
    return render(request, 'pago/confirmar.html', context)


def registrar_pago(request):
    context = {"titulo": "Registrar Pago"}
    return render(request, 'pago/registrar.html', context)

def index(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    oPago=Pago.objects.filter(usuario_id=oUsuario, confirmado=0)

    oPagos_referente=Pago.objects.filter(confirmado_referente=0)


    context={
        'usuario': oUsuario,
        'pagos_referente':oPagos_referente,
        "titulo":"Pagos",
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'horas':plazo_horas(request),
        'pago':oPago,
    }

    return render(request,'pago/index.html',context)
