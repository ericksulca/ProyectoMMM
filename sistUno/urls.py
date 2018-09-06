"""sistUno URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse

from django.contrib.auth.views import logout_then_login
# from password_reset.urls import password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from apps.reset import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Deposito/', include('apps.deposito.urls')),
    path('Pago/', include('apps.pago.urls')),
    path('Solicitud/', include('apps.solicitud.urls')),
    path('Usuario/', include('apps.usuario.urls')),
    path('Testimonio/', include('apps.testimonio.urls')),
    path('', include('apps.home.urls')),
    path('logout', logout_then_login, name='logout'),

    path(r'^recover/(?P<signature>.+)/$', views.recover_done,
        name='password_reset_sent'),
    path(r'^recover/$', views.recover, name='password_reset_recover'),
    path(r'^reset/done/$', views.reset_done, name='password_reset_done'),
    path(r'^reset/(?P<token>[\w:-]+)/$', views.reset,
        name='password_reset_reset'),
    # path('reset/password_reset', password_reset, {'template_name':'reset/password_reset_form.html', 'email_template_name':'reset/password_reset_email.html'}, name='password_reset_recover'),
    # path('reset/password_reset_done', password_reset_done, {'template_name':'reset/password_reset_done.html'}, name='password_reset_done'),
    # path('reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'reset/password_reset_confirm.html'}, name='password_reset_confirm'),
    # path('reset/done', password_reset_complete, {'template_name':'reset/password_reset_complete.html'}, name='password_reset_complete'),

]
