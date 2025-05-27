from django.shortcuts import render, redirect
from .forms import DirectorForm, CategoriaForm, PeliculaForm
from .models import Pelicula

def inicio(request):
    return render(request, "inicio.html")

def agregar_director(request):
    if request.method == "POST":
        formulario = DirectorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = DirectorForm()
    return render(request, "agregar_director.html", {"form": formulario})

def agregar_categoria(request):
    if request.method == "POST":
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = CategoriaForm()
    return render(request, "agregar_categoria.html", {"form": formulario})

def agregar_pelicula(request):
    if request.method == "POST":
        formulario = PeliculaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    else:
        formulario = PeliculaForm()
    return render(request, "agregar_pelicula.html", {"form": formulario})

def buscar_pelicula(request):
    resultado = []
    if "titulo" in request.GET:
        titulo = request.GET["titulo"]
        resultado = Pelicula.objects.filter(titulo__icontains=titulo)
    return render(request, "buscar_pelicula.html", {"peliculas": resultado})
