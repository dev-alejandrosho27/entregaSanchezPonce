class Grupo:
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("grupo")
        
        if not grupo:
            grupo=self.session["grupo"]={}
        else:
            self.grupo=grupo
    def agregar(self, pokemon):
        if (str(pokemon.id) not in self.grupo.keys()):
            self.carro[pokemon.id]={
                "pokemon_id":pokemon.id,
                "nombre":pokemon.nombre,
                "valor":str(pokemon.valor_unitario),
                "imagen":pokemon.imagen.url
                
            }
        else:
            for key, value in self.grupo.item():
                if key==str(pokemon.id):
                    value["valor"]= value["valor"]+1 
                    break
        self.guardar_grupo()
        
        
        
        
        
    def guardar_grupo(self):
        self.session["grupo"]=self.grupo
        self.session.modified=True
    def eliminar_grupo(self,pokemon):
        pokemon.id=str(pokemon.id)
        if pokemon.id in self.grupo:
            del self.grupo[pokemon.id]
            self.guardar_grupo()
    def restar_pokemon(self, pokemon):
        for key, value in self.grupo.item():
                if key==str(pokemon.id):
                    value["valor"]= value["valor"]-1 
                    if  value["valor"]<1:
                        self.eliminar_grupo(pokemon)
                    break
        self.guardar_grupo()
    def vaciar_grupo(self):
        self.session["grupo"]={}
        self.session.modified=True