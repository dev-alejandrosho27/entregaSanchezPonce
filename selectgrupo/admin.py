from django.contrib import admin
from .models import Pokemons,EstadisticasPokemon,TipoPokemon
# Register your models here.





class TiposPokemonAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

class EstadisticasPokemonAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    

class PokemonAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")
    
    
    
admin.site.register(Pokemons,PokemonAdmin)
    
admin.site.register(EstadisticasPokemon,EstadisticasPokemonAdmin)
    
admin.site.register(TipoPokemon,TiposPokemonAdmin)