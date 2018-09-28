from django.urls import path
from django.contrib import admin


from apps.notificacion import views

app_name='notificacion'
urlpatterns = [
    path('leer/<int:id>', views.leer, name='leer'),
]
