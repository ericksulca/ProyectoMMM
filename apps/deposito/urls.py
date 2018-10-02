from django.urls import path

from django.contrib.auth.decorators import login_required
from . import views

app_name='deposito'
urlpatterns = [
    path('operaciones/index', views.index, name='index'),
    path('operaciones/nueva/', login_required(views.deposito_usuario), name='deposito_usuario'),
    path('', login_required(views.deposito_solicitud), name='deposito_solicitud'),
    path('operaciones/listar/', login_required(views.operaciones_usuario), name='operaciones_usuario'),
    path('operaciones/listar-chart/', login_required(views.operaciones_usuario_chart), name='operaciones_usuario_chart'),
    path('confirmar_deposito/<int:id>', views.confirmar_deposito, name='confirmar_deposito'),
]
