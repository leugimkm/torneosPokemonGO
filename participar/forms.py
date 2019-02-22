from django import forms
from django.contrib.auth.models import User
from .models import  Participar

class ParticiparForm(forms.ModelForm):
    class Meta:
        model = Participar
        fields = ['asistir']
      
    