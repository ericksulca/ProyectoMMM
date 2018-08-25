from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect, render_to_response

from apps.home.models import Banner
from .forms import NuevoUsuarioForm
from .models import Usuario, Entidad_bancaria

# Create your views here.


def principal_usuario(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario = ''
    return render(request, 'usuario/principal.html',{'usuario':oUsuario})

def perfil_usuario(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
        oUser = request.user
        oEntidad = Entidad_bancaria.objects.all()
    else:
        oUsuario = ''
    return render(request, 'usuario/perfil.html',{'usuario':oUsuario,'user':oUser,'entidad':oEntidad})


def editar_usuario(request):
    return render(request, 'usuario/editar.html')


def registrar_usuario(request, dni_referido=''):
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
            usuario = authenticate(request, username=username, password=password1)
            login(request, usuario)

            return redirect('usuario:principal')
    else:
        formUsuario = NuevoUsuarioForm(initial={'dni_referido': dni_referido})

    banner = Banner.objects.all()
    context = {
        'formUsuario': formUsuario,
        'banner':banner,
    }

    return render(request, 'usuario/registrar.html', context=context)


def buscar_usuario(request):
    if request.method == 'POST':
        if 'busqueda' in request.POST:
            palabras_busqueda = request.POST['busqueda'].split()
        else:
            palabras_busqueda = ['']
    else:
        palabras_busqueda = ['']
    
    # Función Q importada para hacer consultas complejas, en este caso una consulta con 'OR'
    for busqueda in palabras_busqueda:
        usuarios = Usuario.objects.filter(
            Q(nombres__startswith = busqueda) |
            Q(apellido_paterno__startswith = busqueda) |
            Q(apellido_materno__startswith = busqueda) |
            Q(dni__startswith = busqueda)
            )
        print(usuarios)

    context = {
        'usuarios': usuarios
    }

    return render(request, 'usuario/buscar.html', context)


def validar_email(request):
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            email = ''
    else:
        email = ''
    
    emails = User.objects.values_list('email', flat=True).filter(email=email)

    return render(request, 'usuario/validar_email.html', {'emails': emails})


def validar_username(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            username = ''
    else:
        username = ''
    
    users = User.objects.filter(username=username)
    
    return render(request, 'usuario/validar_username.html', {'users': users})