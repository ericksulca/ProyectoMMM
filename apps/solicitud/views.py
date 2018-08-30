
from django.shortcuts import render

from apps.usuario.models import Usuario

# Create your views here.

def index_solicitud(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario = ''
    context = {
        'usuario': oUsuario
    }

    return render(request, 'solicitud/index.html', context)

def editar_solicitud(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario = ''
    context = {
        'usuario': oUsuario
    }

    return render(request, 'solicitud/editar.html', context)


def nueva_solicitud(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario = ''
    context = {
        'usuario': oUsuario
    }

    return render(request, 'solicitud/nueva.html', context)
