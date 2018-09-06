from django import forms

from .models import Operacion

class NuevoDeposito(forms.ModelForm):

    class Meta:
        model = Operacion

        fields = [
            'monto',
            'usuario_receptor',
        ]

        labels = {
            'monto': 'Monto',
            'usuario_receptor': 'Usuario Receptor',
        }

        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control-p'}),
            'usuario_receptor': forms.Select(attrs={'class': 'form-control-p'}),
        }