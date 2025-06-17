from django import forms
from .models import Mensaje
from django.contrib.auth.models import User

class MensajeForm(forms.ModelForm):
    destinatario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Para",
        widget=forms.Select()
    )

    class Meta:
        model = Mensaje
        fields = ['destinatario', 'asunto', 'contenido']
        widgets = {
            'asunto': forms.TextInput(attrs={'placeholder': 'Asunto'}),
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribí tu mensaje'}),
        }
