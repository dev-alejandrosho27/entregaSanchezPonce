from django.urls import path
from . import views


urlpatterns = [
    
    path("", views.blog, name="Blog"),
    path("tipos/<int:tipos_id>/",views.tipos, name="tipos")
   
]


