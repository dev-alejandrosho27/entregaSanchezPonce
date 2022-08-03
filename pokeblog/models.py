from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tipos(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Tipo"
        verbose_name_plural="Tipos"
    def __str__(self):
        return self.nombre
    
class Reviews(models.Model):
    
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=1000)
    imagen=models.ImageField(upload_to="pokeblog",null=True,blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    tipos=models.ManyToManyField(Tipos)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="Review"
        verbose_name_plural="reviews"
    def __str__(self):
        return self.titulo
    
    
