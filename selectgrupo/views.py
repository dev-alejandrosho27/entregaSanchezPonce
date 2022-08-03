from django.shortcuts import render
from .models import Pokemons

# Create your views here.


def tienda(request):
    
    pokemons=Pokemons.objects.all()
    
    
    return render(request,"selectgrupo/tienda.html",{"poke_lista":pokemons})

