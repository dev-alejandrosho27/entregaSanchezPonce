from django.urls import path
from . import views
from django.conf import Settings, settings
from django.conf.urls.static import static




urlpatterns = [
  
    path("", views.contactos, name="contactos"),
]


