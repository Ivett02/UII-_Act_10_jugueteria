from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'edad', 'direccion', 'telefono']
        labels = {
            'nombre': 'Nombre', 
            'apellido': 'Apellido',
            'edad': 'Edad',
            'direccion': 'Direccion', 
            'telefono': 'Telefono'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}), 
            'apellido': forms.TextInput(attrs={'class': 'form-control'}), 
            'edad': forms.NumberInput(attrs={'class': 'form-control'}), 
            'direccion': forms.TextInput(attrs={'class': 'form-control'}), 
            'telefono': forms.NumberInput(attrs={'class': 'form-control'}), 
        }