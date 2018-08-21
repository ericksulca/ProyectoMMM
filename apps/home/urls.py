from django.urls import path

from apps.home import views

app_name='home'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', views.index, name='index'),

]
