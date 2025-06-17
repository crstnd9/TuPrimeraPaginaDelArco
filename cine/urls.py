from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about/', views.about, name='about'),
    path('peliculas/', views.PeliculaListView.as_view(), name='pelicula_list'),
    path('peliculas/<int:pk>/', views.detalle_pelicula_con_reseñas, name='detalle_con_reseñas'),
    path('peliculas/crear/', views.PeliculaCreateView.as_view(), name='pelicula_create'),
    path('peliculas/<int:pk>/editar/', views.PeliculaUpdateView.as_view(), name='pelicula_update'),
    path('peliculas/<int:pk>/eliminar/', views.PeliculaDeleteView.as_view(), name='pelicula_delete'),
    path('resenas/<int:pk>/editar/', views.editar_resena, name='editar_resena'),
    path('resenas/<int:pk>/eliminar/', views.eliminar_resena, name='eliminar_resena'),
]
