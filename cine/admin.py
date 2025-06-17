from django.contrib import admin
from .models import Director, Categoria, Pelicula, Reseña

admin.site.register(Director)
admin.site.register(Categoria)
admin.site.register(Pelicula)
admin.site.register(Reseña)
