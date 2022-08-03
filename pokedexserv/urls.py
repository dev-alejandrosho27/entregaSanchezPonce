from django.urls import path
from pokedex import views
from django.conf import Settings, settings
from django.conf.urls.static import static
from pokedexserv.views import servicio









urlpatterns = [
    
   path("", servicio , name="Servicios"),
   
   
   
   
]