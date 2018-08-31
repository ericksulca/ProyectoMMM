from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from apps.testimonio.models import Testimonio
from apps.usuario.models import Usuario

def testimonio_registrar(request):
    if request.user.is_authenticated:
        oUsuario = Usuario.objects.get(usuario_login_id=request.user.id)
        try:
            oTestimonio=Testimonio.objects.get(usuario_id=oUsuario.dni)
        except Testimonio.DoesNotExist:
            oTestimonio=None
    else:
        oUsuario = ''

    if request.method=='POST':
        if request.POST['action']=='create':
            form=Testimonio(contenido=request.POST['contenido'],
                            usuario_id=oUsuario.dni)
            form.save()
            success='El testimonio fue guardado correctamente.'
        else:
            oTestimonio.contenido=request.POST['contenido']
            oTestimonio.save()
            success='El testimonio fue modificado correctamente.'
        # return redirect('testimonio:testimonio_registrar')
    else:
        form=''
        success=''

    context = {
        'usuario':oUsuario,
        'testimonio':oTestimonio,
        'respuesta':success
    }

    return render(request, 'testimonio/crear.html',context)
