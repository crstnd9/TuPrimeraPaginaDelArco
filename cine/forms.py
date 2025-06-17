from django import forms
from .models import Director, Categoria, Pelicula, Reseña

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['texto']
        widgets = {
            'texto': forms.Textarea(attrs={'placeholder': 'Escribí tu reseña...'}),
        }
