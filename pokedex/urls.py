from django.urls import path
from pokedex import views
from django.conf import Settings, settings
from django.conf.urls.static import static




urlpatterns = [
    
    path("", views.home, name="Home"),
    
    
  
  
]


urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)