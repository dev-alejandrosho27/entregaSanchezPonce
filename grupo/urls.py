from django.urls import path
from . import views
from django.conf import Settings, settings
from django.conf.urls.static import static



app_name="grupo"
urlpatterns = [
  
    path("agregar/<int:pokemon_id>", views.agregar_pokemon, name="agregar"),
    path("eliminar/<int:pokemon_id>", views.eliminar_pokemon, name="eliminar"),
    path("restar/<int:pokemon_id>", views.restar_pokemon, name="restar"),
    path("limpiar/", views.limpiar_grupo, name="limpiar"),
]


