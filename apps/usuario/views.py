from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core import serializers
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect, render_to_response
from django.contrib import messages

from apps.home.models import Banner
from apps.testimonio.models import Testimonio
from apps.general.models import General
from apps.notificacion.models import Notificacion
from apps.deposito.models import Operacion
from .forms import NuevoUsuarioForm, EditarPerfilForm
from .models import Usuario, Entidad_bancaria

# Create your views here.
from django.db.models import Q

def notificaciones_usuario(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    # oNotificaciones=Notificacion.objects.filter(id_receptor=oUsuario.dni).order_by('-id')#[:5]
    oNotificaciones = Notificacion.objects.filter(
                Q(id_receptor = oUsuario.id) |
                Q(id_emisor_id = oUsuario.id) &
                Q(usuario_sesion=oUsuario.id)
                ).order_by('-id')
    return oNotificaciones

def plazo_horas(request):
    horas=General.objects.get(id=1)
    return horas

def cantidad_notificaciones(request):
    oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    cNotificaciones=Notificacion.objects.filter(id_receptor=oUsuario.id,estado=0).count()
    return cNotificaciones

def gestionar_usuarios(request):
    if request.user.is_staff:
        gestionar=True
    else:
        gestionar=False
        
    return gestionar

def principal_usuario(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
        oOperaciones = Operacion.objects.filter(usuario_receptor=oUsuario).only('id','monto', 'fecha', 'tipo_movimiento', 'usuario_emisor', 'saldo_inicial', 'saldo_final','estado').order_by('-id')
        deposito_realizar=Notificacion.objects.filter(usuario_sesion=oUsuario.id, confirmado=0,tipo="deposito_realizado_emisor")
    else:
        oUsuario = ''
        oOperaciones=''
        deposito_realizar=''
    context={
        'notificaciones':notificaciones_usuario(request),
        'usuario':oUsuario,
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'operaciones':oOperaciones,
        'deposito_realizar':deposito_realizar,
        'horas':plazo_horas(request),
        'gestionar_usuarios':gestionar_usuarios(request),
    }

    return render(request, 'usuario/principal.html',context)

def perfil_usuario(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
        oUser = request.user
        # formUsuario = EditarPerfilForm(instance=oUsuario)

        if request.method == 'POST':
            formUsuario = EditarPerfilForm(request.POST, instance=oUsuario)
            if formUsuario.is_valid():
                usuario = formUsuario.save(commit=False)

            if 'foto_perfil' in request.FILES:
                usuario.foto_perfil = request.FILES['foto_perfil']

            usuario.save()
            # Redirect
        else:
            formUsuario = EditarPerfilForm(instance=oUsuario)

    else:
        oUsuario = ''

    context = {
        'usuario': oUsuario,
        'user': oUser,
        'formUsuario': formUsuario,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'horas':plazo_horas(request),
    }
    return render(request, 'usuario/perfil/perfil.html',context)

def cambio_contrasena(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
        oUser = request.user
        if request.method == 'POST':
            form = PasswordChangeForm(data=request.POST, user=oUser)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.add_message(request, messages.INFO, "success")
                return redirect('usuario:cambio_contraseña')

            else:
                messages.add_message(request, messages.INFO, "error")
                return redirect('usuario:cambio_contraseña')
        else:
            form = PasswordChangeForm(user=oUser)

    context = {
        'usuario': oUsuario,
        'user': oUser,
        'form': form,
        'notificaciones':notificaciones_usuario(request),
        'cantidad_notificaciones':cantidad_notificaciones(request),
        'gestionar_usuarios':gestionar_usuarios(request),
        'horas':plazo_horas(request),
    }

    return render(request, 'usuario/perfil/cambio_contraseña.html', context)

def editar_usuario(request):
    return render(request, 'usuario/editar.html')

def registrar_usuario(request, dni_referido=''):
    if request.method == 'POST':
        formUsuario = NuevoUsuarioForm(request.POST, request.FILES)
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # try:
        #     a=formUsuario.is_valid()
        #     print (a)
        # except

        # and formUsuario.is_valid()
        if password1 == password2 and formUsuario.is_valid():
            try:
                user = User.objects.create_user(username, email, password1)
            except IntegrityError as e:
                return e.__cause__
            usuario = formUsuario.save(commit=False)
            usuario.usuario_login = user
            usuario.save()


            # usuario_admin=Usuario.objects.get(dni=37847637)
            # BUSCA EL USUARIO PERTENECIENTE AL USER ADMIN

            #Nube
            usuario_admin=Usuario.objects.get(usuario_login_id=4)
            #Local
            # usuario_admin=Usuario.objects.get(usuario_login_id=1)

            saldo_usuario = Operacion(monto=0.00, saldo_inicial=0.00, saldo_final=0.00, usuario_emisor=usuario, usuario_receptor=usuario, tipo_movimiento='Registro')
            saldo_usuario.save()

            # OBTIENE EL COSTO DE INSCRIPCION Y OTROS
            monto_registro=General.objects.get(id=1)

            ultima_operacion_receptor = Operacion.objects.filter(usuario_receptor=usuario_admin).latest(field_name='fecha')
            saldo_final_anterior_receptor = ultima_operacion_receptor.saldo_final
            Saldo_final_operacion_receptor = ultima_operacion_receptor.saldo_final + monto_registro.inscripcion
            deposito_defecto = Operacion(monto=20.00, saldo_inicial=saldo_final_anterior_receptor, saldo_final=Saldo_final_operacion_receptor, usuario_emisor=usuario, usuario_receptor=usuario_admin, tipo_movimiento='Solicitud')
            deposito_defecto.save()

            notificacion=Notificacion(
                id_emisor_id=usuario_admin.id,
                id_receptor=usuario.id,
                usuario_sesion=usuario.id,
                tipo='deposito_realizado_emisor',
                estado=0,
                monto=monto_registro.inscripcion,
                confirmado=0
            )
            notificacion.save()

            usuario = authenticate(request, username=username, password=password1)
            login(request, usuario)

            return redirect('usuario:principal')

        else:
            return redirect('usuario:registrar_usuario')
    else:
        formUsuario = NuevoUsuarioForm(initial={'dni_referido': dni_referido})
        if dni_referido == '':
            oReferido=''
        else:
            oReferido=Usuario.objects.get(dni=dni_referido)

        # formUsuario = NuevoUsuarioForm(initial={'dni_referido': oReferido.id})


    banner = Banner.objects.all()
    testimonio=Testimonio.objects.all()
    context = {
        'formUsuario': formUsuario,
        'banner':banner,
        'testimonio':testimonio,
        'dni_referido':dni_referido,
        'referido':oReferido,
        # 'dni_referido':dni_referido,
    }

    return render(request, 'usuario/registrar/registrar.html', context=context)


def buscar_usuario(request):
    if request.method == 'POST':

        busqueda=request.POST['busqueda'].split()
        busqueda_reverso=busqueda[::-1]
        tamanio=len(busqueda)

        if tamanio == 1:

            oUsuarios = Usuario.objects.filter(
                        Q(nombres__icontains = request.POST['busqueda']) |
                        Q(apellido_paterno__icontains = request.POST['busqueda']) |
                        Q(apellido_materno__icontains = request.POST['busqueda']) |
                        Q(dni__icontains= request.POST['busqueda'])
                        # Q(id= request.POST['busqueda'])
                        )
        elif tamanio == 2:
            oUsuarios = Usuario.objects.filter(
                        Q(nombres__icontains = busqueda_reverso[1]) &
                        Q(apellido_paterno__icontains = busqueda_reverso[0])

                        )
        else:
            oUsuarios = Usuario.objects.filter(
                        Q(nombres__icontains = busqueda_reverso[2]) &
                        Q(apellido_paterno__icontains = busqueda_reverso[1]) &
                        Q(apellido_materno__icontains = busqueda_reverso[0])
                        )

    else:
        palabras_busqueda = ['']
        oUsuario=''

    data = serializers.serialize(
                'json',
                oUsuarios
            )
    return HttpResponse(data, content_type='application/json')

def buscar_usuario_id(request):
    if request.method == 'POST':
        oUsuario=Usuario.objects.filter(id=request.POST['busqueda'])
    else:
        oUsuario=''
    data = serializers.serialize(
                'json',
                oUsuario
            )
    return HttpResponse(data, content_type='application/json')

def buscar_usuario_confirmacion(request,id_usuario):
    oUsuario=Usuario.objects.filter(id=id_usuario)


    context = {
        'usuarios': oUsuario
    }
    data = serializers.serialize(
            'json',
            oUsuario,
            fields = ['nombres','apellido_paterno','apellido_materno']
        )
    return HttpResponse(data, content_type='application/json')

def validar_email(request):
    if request.method == 'POST':
        if 'email' in request.POST:
            email = request.POST['email']
        else:
            email = ''
    else:
        email = ''

    emails = User.objects.values_list('email', flat=True).filter(email=email)

    return render(request, 'usuario/registrar/validar_email.html', {'emails': emails})

def validar_username(request):
    if request.method == 'POST':
        if 'username' in request.POST:
            username = request.POST['username']
        else:
            username = ''
    else:
        username = ''

    users = User.objects.filter(username=username)

    return render(request, 'usuario/registrar/validar_username.html', {'users': users})
