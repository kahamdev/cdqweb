from .models import Suscribe
from django import forms

class SuscribeForm(forms.ModelForm):
    class Meta:
        model=Suscribe
        fields="__all__"