from django import forms
from django.core.files.images import ImageFile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Usuario

class NuevoUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'dni',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'foto_perfil',
            'dni_referido',
            'numero_cuenta',
            'entidad_bancaria',
        ]

        labels = {
            'dni': 'DNI',
            'nombres': 'Nombre(s)',
            'apellido_paterno': 'Apellido paterno',
            'apellido_materno': 'Apellido materno',
            'foto_perfil': 'Foto de perfil',
            'dni_referido': 'DNI del referente',
            'numero_cuenta':'Numero de cuenta',
            'entidad_bancaria': 'Entidad bancaria',
        }

        widgets = {
            'dni': forms.NumberInput(attrs={'class': 'form-control-p'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control-p'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control-p'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control-p'}),
            'foto_perfil': forms.FileInput(),
            'dni_referido': forms.NumberInput(attrs={'class': 'form-control-p'}),
            'numero_cuenta': forms.NumberInput(attrs={'class': 'form-control-p'}),
            'entidad_bancaria': forms.Select(attrs={'class': 'form-control-p'}),
        }
