from django.urls import path
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from apps.testimonio import views

app_name='testimonio'
urlpatterns = [
    path('', login_required(views.testimonio_registrar), name='testimonio_registrar'),
]
