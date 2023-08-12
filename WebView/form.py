from .models import Broker
from django import forms

class BrokerForm(forms.ModelForm):
    class Meta:
        model=Broker
        fields=('username','message')    # also "__all__"