from django.urls import path

from . import views

urlpatterns = [
    path('editar/', views.editar_solicitud, name='editar solicitud '),
    path('registrar/', views.registrar_solicitud, name='registrar solicitud'),
]
