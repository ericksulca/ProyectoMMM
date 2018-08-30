from django import forms
from django.core.files.images import ImageFile

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
            'dni': forms.NumberInput(attrs={'class': 'form-control-p', 'placeholder':'DNI','onKeyPress':'if(this.value.length==8) return false;'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control-p', 'placeholder':'Nombres'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control-p', 'placeholder':'Apellido paterno'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control-p', 'placeholder':'Apellido materno'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control-p'}),
            'dni_referido': forms.NumberInput(attrs={'class': 'form-control-p'}),
            'numero_cuenta': forms.NumberInput(attrs={'class': 'form-control-p', 'placeholder':'Número de cuenta'}),
            'entidad_bancaria': forms.Select(attrs={'class': 'form-control-p'}),
        }


class EditarPerfilForm(forms.ModelForm):

    class Meta:
        model = Usuario

        fields = [
            'foto_perfil',
            'nombres',
            'apellido_paterno',
            'apellido_materno',
            'dni',
            'entidad_bancaria',
            'numero_cuenta',
        ]

        labels = {
            'foto_perfil': 'Nueva foto de perfil',
            'nombres': 'Nombres',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'dni': 'DNI',
            'entidad_bancaria': 'Entidad Bancaria',
            'numero_cuenta': 'Numero de cuenta'
        }

        widgets = {
            'foto_perfil': forms.FileInput(attrs={'class': 'form-control'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'entidad_bancaria': forms.Select(attrs={'class': 'form-control'}),
            'numero_cuenta': forms.NumberInput(attrs={'class': 'form-control'})
        }