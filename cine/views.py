from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Pelicula
from .forms import PeliculaForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")

def buscar_pelicula(request):
    return render(request, "buscar_pelicula.html")

class PeliculaListView(ListView):
    model = Pelicula
    template_name = "cine/pelicula_list.html"
    context_object_name = "peliculas"

    def get_queryset(self):
        queryset = super().get_queryset()
        titulo = self.request.GET.get("titulo")
        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = self.request.GET.get("titulo", "")
        return context

class PeliculaDetailView(DetailView):
    model = Pelicula
    template_name = "cine/pelicula_detail.html"
    context_object_name = "pelicula"

class PeliculaCreateView(LoginRequiredMixin, CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "cine/pelicula_form.html"
    success_url = reverse_lazy('pelicula_list')

class PeliculaUpdateView(LoginRequiredMixin, UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = "cine/pelicula_form.html"
    success_url = reverse_lazy('pelicula_list')

class PeliculaDeleteView(LoginRequiredMixin, DeleteView):
    model = Pelicula
    template_name = "cine/pelicula_confirm_delete.html"
    success_url = reverse_lazy('pelicula_list')
