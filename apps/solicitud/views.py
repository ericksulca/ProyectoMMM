from django.shortcuts import render

# Create your views here.

def editar_solicitud(request):
    return render(request, 'solicitud/editar.html')


def registrar_solicitud(request):
    return render(request, 'solicitud/registrar.html')
