from django.shortcuts import render, redirect

from apps.usuario.forms import NuevoUsuarioForm
from apps.home.models import Banner

def index(request):
    if request.method=='POST':
        form=NuevoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home:index')
    else:
        form=NuevoUsuarioForm()

    banner = Banner.objects.all()

    return render(request, 'home/index.html',{'form':form,'banner':banner})
