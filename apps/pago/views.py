from django.shortcuts import render

# Create your views here.

def confirmar_pago(request):
    context = {"titulo": "Confirmar Pago"}
    return render(request, 'pago/confirmar.html', context)


def registrar_pago(request):
    context = {"titulo": "Registrar Pago"}
    return render(request, 'pago/registrar.html', context)