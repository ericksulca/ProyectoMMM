from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.usuario.forms import NuevoUsuarioForm
from apps.home.models import Banner
from apps.usuario.models import Usuario
from apps.testimonio.models import Testimonio
from apps.articulo.models import Articulo

def index(request):
    mensaje=''
    if request.method == 'POST':
        if 'username' in request.POST and 'contraseña' in request.POST:
            username = request.POST['username']
            password = request.POST['contraseña']
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)

                return redirect('usuario:principal')

            else:
                # redirect('home:index')
                mensaje='Usuario o contraseña incorrecta'
        else:
            username = 'no hay usuario'
            password = 'no hay password'

    banner = Banner.objects.all()
    testimonio=Testimonio.objects.all()


    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''

    oArticulo=Articulo.objects.all()[:4]
    context={
        'mensaje':mensaje,
        'banner':banner,
        'usuario':oUsuario,
        'testimonio':testimonio,
        'articulo':oArticulo,
    }

    return render(request, 'home/index.html',context)
