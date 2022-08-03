from operator import truediv
from django.db import models

# Create your models here.


class TipoPokemon(models.Model):
    tipo=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Tipo"
        verbose_name_plural="Tipos"
    def __str__(self):
        return self.tipo
    
class EstadisticasPokemon(models.Model):
    
    atk=models.IntegerField()
    defen=models.IntegerField()
    spp=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name="Estadistica"
        verbose_name_plural="Estadisticas"
    def __str__(self):
        return "atk {} def {} spp {}".format(self.atk,self.defen,self.spp)
    
class Pokemons(models.Model):
    nombre=models.CharField(max_length=30)
    tipo=models.ForeignKey(TipoPokemon,on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="selectgrupo",null=True,blank=True)
    descripcion=models.CharField(max_length=1000,)
    peso=models.FloatField()
    estadisticas=models.ManyToManyField(EstadisticasPokemon)
    evolucion=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    valor_unitario=models.IntegerField()
    
    
    
    class Meta:
        verbose_name="pokemon"
        verbose_name_plural="pokemons"

