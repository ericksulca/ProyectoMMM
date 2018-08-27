from django.urls import path
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from . import views


app_name='usuario'
urlpatterns = [
    path('buscar-usuario/', views.buscar_usuario, name='buscar_usuario'),
    path('editar/', login_required(views.editar_usuario), name='editar_usuario'),
    # path('login/', views.login_usuario, name='login'),
    path('principal/', login_required(views.principal_usuario), name='principal'),
    path('perfil/', login_required(views.perfil_usuario), name='perfil'),
    path('perfil/cambio-contraseña', login_required(views.cambio_contraseña), name='cambio_contraseña'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('registrar/<int:dni_referido>/', views.registrar_usuario, name='registrar_usuario_ref'),
    path('validar-username/', views.validar_username, name='validar_username'),
    path('validar-email/', views.validar_email, name='validar_email'),
    path('saldo/listar/', views.saldos_usuario, name='saldos_usuario')
]
