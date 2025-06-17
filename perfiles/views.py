from django.shortcuts import render, redirect
from .models import Perfil
from .forms import PerfilFormulario, RegistroFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required
def perfil_usuario(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'perfiles/perfil.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        formulario = PerfilFormulario(request.POST, request.FILES, instance=perfil)
        if formulario.is_valid():
            formulario.save()
            return redirect('perfil')
    else:
        formulario = PerfilFormulario(instance=perfil)

    return render(request, 'perfiles/editar_perfil.html', {'formulario': formulario})

def registro(request):
    if request.method == 'POST':
        formulario = RegistroFormulario(request.POST)
        if formulario.is_valid():
            usuario = formulario.save()
            login(request, usuario)
            return redirect('perfil')
    else:
        formulario = RegistroFormulario()

    return render(request, 'perfiles/registro.html', {'formulario': formulario})
