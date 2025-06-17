from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from .forms import MensajeForm
from django.contrib.auth.models import User

@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha')
    return render(request, "mensajes/bandeja_entrada.html", {"mensajes": mensajes})

@login_required
def detalle_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(Mensaje, id=mensaje_id, destinatario=request.user)
    return render(request, "mensajes/detalle_mensaje.html", {"mensaje": mensaje})

@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect("bandeja_entrada")
    else:
        form = MensajeForm()
    return render(request, "mensajes/enviar_mensaje.html", {"form": form})
