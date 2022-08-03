from django.shortcuts import render
from pokedexserv.models import PokemonServ

# Create your views here.
def servicio(request):
    pokemon=PokemonServ.objects.all()
    return render(request,"pokedexserv/servicios.html", {"pokemon":pokemon})