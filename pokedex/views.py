from django.shortcuts import render,HttpResponse
from pokedexserv.models import PokemonServ
# Create your views here.



def home(request):
    return render(request,"pokedex/home.html")





