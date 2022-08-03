from email.headerregistry import ContentDispositionHeader
from django.db import models
from django.forms import CharField

# Create your models here.

class PokemonServ(models.Model):
    tipo=models.CharField(max_length=20)
    peso=models.IntegerField(null=True,blank=True)
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="pokedexserv")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="pokedex"
        verbose_name_plural="pokedex"
    def __str__(self):
        return self.titulo
    