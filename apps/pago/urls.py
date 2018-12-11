from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
app_name='pago'

urlpatterns = [
    path('confirmar/', views.confirmar_pago, name='confirmar pago'),
    path('registrar/', views.registrar_pago, name='registrar pago'),
    path('', login_required(views.index), name='lista_pagos'),
]
