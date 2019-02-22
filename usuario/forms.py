from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ELEGIR_SEXO, ELEGIR_TEAM, Profile

from django.forms import PasswordInput

class UserRegisterForm(UserCreationForm):
    sexo = forms.ChoiceField(choices=ELEGIR_SEXO, required=True)
    team = forms.ChoiceField(choices=ELEGIR_TEAM, required=True,)
    class Meta:
        model = User
        fields = ['username','sexo','team','password1', 'password2']
        labels = {
            'username': 'usuario',
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': "form-control",
            }),
            'password1': forms.TextInput(attrs={
                'type': "password",
                'class': "form-control",
            }),
            'password2': forms.TextInput(attrs={
                'type': "password",
                'class': "form-control",
            })
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        
        
        self.fields['username'].help_text = "Requerido. De 4 a 15 caracteres. Solo letras y digitos."
        self.fields['password1'].widget = PasswordInput(attrs={'class':'form-control'})
        self.fields['password1'].label = "contraseña"
        self.fields['password1'].help_text = "La contraseña debe ser por lo menos de 8 caracteres"
        self.fields['password2'].widget = PasswordInput(attrs={'class':'form-control'})
        self.fields['password2'].label = "Verificar contraseña"
        self.fields['password2'].help_text = "Volver a ingresar la contraseña para verificarla" 


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'usuario',
        }
      
    
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nivel']
      
    