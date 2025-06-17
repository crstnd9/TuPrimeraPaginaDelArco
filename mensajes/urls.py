from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja_entrada, name='mensajes'),
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('bandeja/', views.bandeja_entrada, name='bandeja_entrada'),
    path('mensaje/<int:mensaje_id>/', views.detalle_mensaje, name='detalle_mensaje'),
]
