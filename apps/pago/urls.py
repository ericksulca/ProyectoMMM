from django.urls import path

from . import views

urlpatterns = [
    path('confirmar/', views.confirmar_pago, name='confirmar pago'),
    path('registrar/', views.registrar_pago, name='registrar pago'),
]
