from django.urls import path
from django.contrib import admin

from . import views

app_name='usuario'
urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('editar/', views.editar_usuario, name='editar_usuario '),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    path('buscar-usuario/', views.buscar_usuario, name='buscar_usuario'),
]
