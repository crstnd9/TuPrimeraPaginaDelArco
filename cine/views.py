from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Pelicula, Reseña
from .forms import PeliculaForm, ReseñaForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def inicio(request):
    return render(request, "inicio.html")

def about(request):
    return render(request, "about.html")

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

@login_required
def detalle_pelicula_con_reseñas(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    resenas = pelicula.resenas.all().order_by('-fecha')

    if request.method == "POST":
        form = ReseñaForm(request.POST)
        if form.is_valid():
            nueva_resena = form.save(commit=False)
            nueva_resena.pelicula = pelicula
            nueva_resena.usuario = request.user
            nueva_resena.save()
            return redirect('detalle_con_reseñas', pk=pelicula.pk)
    else:
        form = ReseñaForm()

    return render(request, "cine/pelicula_detail.html", {
        "pelicula": pelicula,
        "resenas": resenas,
        "formulario": form
    })

@login_required
def editar_resena(request, pk):
    resena = get_object_or_404(Reseña, pk=pk)
    if request.user != resena.usuario:
        return HttpResponseForbidden("No tenés permiso para editar esta reseña.")

    if request.method == 'POST':
        form = ReseñaForm(request.POST, instance=resena)
        if form.is_valid():
            form.save()
            return redirect('detalle_con_reseñas', pk=resena.pelicula.pk)
    else:
        form = ReseñaForm(instance=resena)

    return render(request, 'cine/editar_resena.html', {'form': form, 'resena': resena})

@login_required
def eliminar_resena(request, pk):
    resena = get_object_or_404(Reseña, pk=pk)
    if request.user != resena.usuario:
        return HttpResponseForbidden("No tenés permiso para eliminar esta reseña.")

    if request.method == 'POST':
        pelicula_id = resena.pelicula.pk
        resena.delete()
        return redirect('detalle_con_reseñas', pk=pelicula_id)

    return render(request, 'cine/eliminar_resena.html', {'resena': resena})
