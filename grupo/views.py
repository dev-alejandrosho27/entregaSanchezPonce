from django.shortcuts import render,redirect
from .grupo import Grupo
from selectgrupo.models import Pokemons
# Create your views here.




def agregar_pokemon(request,pokemon_id):
    grupo=Grupo(request)
    pokemon=Pokemons.objects.get(id=pokemon_id)
    grupo.agregar(pokemon=pokemon)
    return redirect("tienda")
def eliminar_pokemon(request,pokemon_id):
    grupo=Grupo(request)
    pokemon=Pokemons.objects.get(id=pokemon_id)
    grupo.eliminar_grupo(pokemon=pokemon)
    return redirect("tienda")
def restar_pokemon(request,pokemon_id):
    grupo=Grupo(request)
    pokemon=Pokemons.objects.get(id=pokemon_id)
    grupo.restar_pokemon(pokemon=pokemon)
    return redirect("tienda")
def limpiar_grupo(request,pokemon_id):
    grupo=Grupo(request)
    grupo.vaciar_grupo()
    return redirect("tienda")