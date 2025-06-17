from django.urls import path
from . import views

urlpatterns = [
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('registro/', views.registro, name='registro'),
    path('ver/<str:username>/', views.perfil_publico, name='perfil_publico'),
]
