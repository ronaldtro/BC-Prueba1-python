from django.contrib import admin

from .models import Director, Genre, Pelicula, PeliculaInstance, Restriccion

admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Restriccion)
admin.site.register(Pelicula)
admin.site.register(PeliculaInstance)

