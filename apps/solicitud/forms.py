from django import forms

from .models import Solicitud

class NuevaSolicitudForm(forms.ModelForm):

    class Meta:
        model = Solicitud

        fields = [
            'monto',
        ]
        
        labels = {
            'monto': 'Monto',
        }

        widgets = {
            'monto': forms.NumberInput(attrs={'class': 'form-control-p', 'placeholder': '0.00'}),
        }