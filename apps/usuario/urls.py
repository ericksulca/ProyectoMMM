from django.urls import path
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from . import views


app_name='usuario'
urlpatterns = [
    path('buscar-usuario/', views.buscar_usuario, name='buscar_usuario'),
    path('editar/', views.editar_usuario, name='editar_usuario'),
    # path('login/', views.login_usuario, name='login'),
    path('principal/', login_required(views.principal_usuario), name='principal'),
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),
    
]
