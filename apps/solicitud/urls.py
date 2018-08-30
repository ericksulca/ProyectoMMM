from django.urls import path

from . import views

app_name='solicitud'
urlpatterns = [
    path('', views.index_solicitud, name='index'),
    path('editar/', views.editar_solicitud, name='editar_solicitud'),
    path('nueva/', views.nueva_solicitud, name='nueva_solicitud'),
]
