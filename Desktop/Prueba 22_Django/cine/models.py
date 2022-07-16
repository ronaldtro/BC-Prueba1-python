from audioop import reverse
import uuid
from django.db import models

class Director(models.Model):
    nombres = models.CharField(max_length=40, help_text='Nombres del director')
    apellidos = models.CharField(max_length=40, help_text='Apellidos del director')
    edad = models.CharField(max_length=3, help_text='Edad del director')
    correo = models.CharField(max_length=40, help_text='Correo del director')
    genre = models.CharField(max_length=20, help_text='Genero del director')

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)

    def get_absolute_url(self):
        return reverse('director-detail', args=[str(self.id)]) 

class Pelicula(models.Model):
    nombre = models.CharField(max_length=30, help_text='Nombre de la pelicula')
    sinopsis = models.TextField(max_length=100, help_text='Resumen de la pelicula')
    restriccion = models.ForeignKey('Restriccion', on_delete=models.SET_NULL, null=True)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '%s %s' % (self.nombre, self.sinopsis)

    def get_absolute_url(self):
        return reverse('peliculas-detail', args=[str(self.id)])


class Restriccion(models.Model):
    tipo = models.CharField(max_length=20, help_text='Tipo de restriccion')

    def __str__(self):
        return '%s' % (self.tipo)

    def get_absolute_url(self):
        return reverse('restriccion-detail', args=[str(self.id)])


class Genre(models.Model):
    nombre = models.CharField(max_length=20, help_text='Genero de pelicula')

    def __str__(self):
        return '%s' % (self.nombre)

    def get_absolute_url(self):
        return reverse('genre-detail', args=[str(self.id)])   

class PeliculaInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID de la pelicula')
    pelicula = models.ForeignKey('Pelicula', on_delete=models.SET_NULL, null=True)
    fecha_estreno = models.DateField(null=True, blank=True)

    opciones = (
        ('m', 'Muy pronto'),
        ('c', 'En cartelera'),
    )
    
    estado = models.CharField(max_length=1, choices=opciones, blank=True, default='m', help_text='Estado de pelicula')

    def __str__(self):
        return '%s (%s)' % (self.id, self.pelicula.nombre)     

