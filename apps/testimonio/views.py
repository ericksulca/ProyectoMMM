from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy

from apps.testimonio.models import Testimonio
from apps.usuario.models import Usuario

def testimonio_registrar(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario = ''

    if request.method=='POST':
        form=Testimonio(contenido=request.POST['contenido'],
                        usuario_id=oUsuario.dni)
        form.save()
        return redirect('usuario:principal')
    else:
        form=''

    context = {
        'usuario':oUsuario,
    }
    return render(request, 'testimonio/crear.html',context)
