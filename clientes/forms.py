from django import forms
from django.forms import inlineformset_factory

from .models import (
    Cliente, Veiculo
)


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'
