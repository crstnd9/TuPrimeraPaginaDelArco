from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('peliculas/', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('peliculas/<int:pk>/', views.PeliculaDetailView.as_view(), name='pelicula_detail'),
    path('peliculas/crear/', views.PeliculaCreateView.as_view(), name='pelicula_create'),
    path('peliculas/<int:pk>/editar/', views.PeliculaUpdateView.as_view(), name='pelicula_update'),
    path('peliculas/<int:pk>/eliminar/', views.PeliculaDeleteView.as_view(), name='pelicula_delete'),
    path('buscar/', views.buscar_pelicula, name='buscar_pelicula'),  # <--- ESTA LÍNEA
]
