from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.usuario.forms import NuevoUsuarioForm
from apps.home.models import Banner
from apps.usuario.models import Usuario
from apps.testimonio.models import Testimonio
from apps.articulo.models import Articulo
from apps.solicitud.models import Solicitud
from apps.general.models import General

from django.core.mail import EmailMessage
from django.shortcuts import render_to_response

from django.db.models import Q

def baner_testimonio(request):
    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''

    banner = Banner.objects.all()
    testimonio=Testimonio.objects.all()
    legalidad=Articulo.objects.get(categoria_id=3)
    quienes_somos=Articulo.objects.get(categoria_id=4)
    entidad_financiera=Articulo.objects.get(categoria_id=5)
    context={
        'usuario':oUsuario,
        'banner':banner,
        'testimonio':testimonio,
        'legalidad':legalidad,
        'quienes_somos':quienes_somos,
        'entidad_financiera':entidad_financiera,
    }
    return context

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

    oArticulo_p=Articulo.objects.filter(categoria_id=1).order_by('-id')
    oArticulo_s=Articulo.objects.filter(categoria_id=2).order_by('-id')[:3]

    video=General.objects.get(id=1)
    context={
        'mensaje':mensaje,
        'banner':banner,
        'usuario':oUsuario,
        'testimonio':testimonio,
        'articulo_p':oArticulo_p,
        'articulo_s':oArticulo_s,
        'video':video.enlace_youtube,
    }

    return render(request, 'home/index.html',context)


def legalidad(request):
    return render(request,'home/legalidad.html',baner_testimonio(request))

def quienes_somos(request):
    return render(request,'home/quienes_somos.html',baner_testimonio(request))

def testimonios(request):
    return render(request,'home/testimonios.html',baner_testimonio(request))

def ed_financiera(request):
    return render(request,'home/ed_financiera.html',baner_testimonio(request))

def contactenos(request):
    if request.user.is_authenticated:
        oUsuario=Usuario.objects.get(usuario_login_id=request.user.id)
    else:
        oUsuario=''

    banner = Banner.objects.all()
    testimonio=Testimonio.objects.all()

    if request.method=='POST':
        asunto='Mensaje desde formulario de contacto'
        mensaje='Email: '+request.POST['email']+'.\n Nombre: '+request.POST['nombre']+'.\n Mensaje: \n'+request.POST['mensaje']
        mail=EmailMessage(asunto,mensaje,to=['fincomun.info@gmail.com'])
        mail.send()
        success='success'

        asunto2='Mensaje de contacto recibido'
        mensaje2='Hola '+request.POST['nombre']+', su mensaje:\n'+request.POST['mensaje']+ '\n fue recibido con éxito, responderemos a su consulta en breve.'
        mail2=EmailMessage(asunto2,mensaje2,to=[request.POST['email']])
        mail2.send()

        context={
            'success':success,
            'usuario':oUsuario,
            'banner':banner,
            'testimonio':testimonio,
        }
        return render(request,'home/contactenos.html',context)

    return render(request,'home/contactenos.html',baner_testimonio(request))


# PRUEBA
def prueba(request):
    oUsuario=Usuario.objects.all()
    oSolicitud=Solicitud.objects.all()
    context={
        'usuario':oUsuario,
        'solicitud':oSolicitud,
    }

    return render(request, 'prueba/prueba.html',context)
