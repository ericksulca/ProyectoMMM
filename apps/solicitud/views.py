
from django.shortcuts import render, redirect

from .forms import NuevaSolicitudForm
from apps.usuario.models import Usuario

# Create your views here.

def index_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    
    context = {
        'usuario': oUsuario
    }

    return render(request, 'solicitud/index.html', context)

def editar_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    
    context = {
        'usuario': oUsuario
    }

    return render(request, 'solicitud/editar.html', context)


def nueva_solicitud(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    if request.method == 'POST':
        form = NuevaSolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.usuario = oUsuario
            solicitud.save()
            return redirect('solicitud:index')
        else:
            return redirect('solicitud:nueva_solicitud')
    else:
        form = NuevaSolicitudForm()

    context = {
        'usuario': oUsuario,
        'form': form
    }

    return render(request, 'solicitud/nueva.html', context)