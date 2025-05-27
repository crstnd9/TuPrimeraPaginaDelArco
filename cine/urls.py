from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('agregar_director/', views.agregar_director, name='agregar_director'),
    path('agregar_categoria/', views.agregar_categoria, name='agregar_categoria'),
    path('agregar_pelicula/', views.agregar_pelicula, name='agregar_pelicula'),
    path('buscar_pelicula/', views.buscar_pelicula, name='buscar_pelicula'),
]