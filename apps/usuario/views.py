from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate
from .forms import NuevoUsuarioForm
from .models import Usuario
from apps.home.models import Banner

# Create your views here.


def principal_usuario(request):
    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''
    return render(request, 'usuario/principal.html',{'usuario':oUsuario})

def editar_usuario(request):
    return render(request, 'usuario/editar.html')


def registrar_usuario(request):
    if request.method == 'POST':
        formUsuario = NuevoUsuarioForm(request.POST, request.FILES)
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2 and formUsuario.is_valid():
            try:
                user = User.objects.create_user(username, email, password1)
            except IntegrityError as e:
                return e.__cause__
            usuario = formUsuario.save(commit=False)
            usuario.usuario_login = user
            usuario.save()

            return redirect('home:index')
    else:
        formUsuario = NuevoUsuarioForm()

    banner = Banner.objects.all()
    context = {
        'formUsuario': formUsuario,
        'banner':banner,
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
