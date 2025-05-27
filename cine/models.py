from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_estreno = models.DateField()

    def __str__(self):
        return self.titulo
