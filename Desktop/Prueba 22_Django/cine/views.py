from django.shortcuts import render
from .models import  Director, Genre, Restriccion, Pelicula, PeliculaInstance

def index(request):
    director1 = Director.objects.filter(nombres='Ronald B').get()
    director2 = Director.objects.filter(nombres='Guillermo').get()

    pelicula1 = Pelicula.objects.filter(nombre='El enredo de django').get()
    pelicula2 = Pelicula.objects.filter(nombre='El laberinto del fauno').get()

    num_peliculas = Pelicula.objects.all().count()
    num_Peliculas_publicadas = PeliculaInstance.objects.all().count()
    enCartelera = PeliculaInstance.objects.filter(estado='c').count()
    num_directores = Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'director1': director1,
            'director2': director2,
            'pelicula1': pelicula1,
            'pelicula2': pelicula2,
        },
    )