from django import forms
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PerfilFormulario(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'bio']

class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
