from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.usuario.forms import NuevoUsuarioForm
from apps.home.models import Banner

def index(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'contraseña' in request.POST:
            username = request.POST['username']
            password = request.POST['contraseña']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('usuario:registrar_usuario')
            else:
                redirect('home:index')
        else:
            username = 'no hay usuario'
            password = 'no hay password'        

    banner = Banner.objects.all()

    return render(request, 'home/index.html',{'banner':banner})
