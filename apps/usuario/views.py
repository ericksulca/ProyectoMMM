from django.shortcuts import render, redirect

from .forms import NuevoUsuarioForm
from .models import Usuario
from apps.home.models import Banner

# Create your views here.

def login_usuario(request):
    return render(request, 'usuario/login.html')

def editar_usuario(request):
    return render(request, 'usuario/editar.html')


def registrar_usuario(request):
    if request.method == 'POST':
        formUsuario = NuevoUsuarioForm(request.POST, request.FILES)
        if formUsuario.is_valid():
            formUsuario.save()
            return redirect('home:index')
    else:
        formUsuario = NuevoUsuarioForm()
    banner = Banner.objects.all()
    context = {
        'formUsuario': formUsuario,'banner':banner,
    }

    return render(request, 'usuario/registrar.html', context=context)


def buscar_usuario(request):
    if request.method == 'POST':
        if 'busqueda' in request.POST:
            busqueda = request.POST['busqueda']
        else:
            busqueda = ''
    else:
        busqueda = ''

    usuarios = Usuario.objects.filter(nombres__contains=busqueda)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'usuario/buscar.html', context)
