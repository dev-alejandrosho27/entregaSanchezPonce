from django.shortcuts import redirect, render
from .forms import FormularioDeEntrenador
from django.core.mail import EmailMessage,send_mail
# Create your views here.

def contactos(request):
    formulario_entrenador=FormularioDeEntrenador()
    
    if request.method =="POST":
        formulario_entrenador=FormularioDeEntrenador(data=request.POST)
        if formulario_entrenador.is_valid():
            nombre=request.POST.get("Nombre")
            email=request.POST.get("Email")
            Descripcion=request.POST.get("Descripcion")
            try:
                send_mail("mensaje desde app django",
                "el usuario con nombre {} con la direccion {} escribe lo siguiente: \n\n {}".format(nombre,email,Descripcion),
                "alejo.san2707@gmail.com",email,fail_silently=False)
        
            
                
                return redirect("/infoentrenador/?valido")
            except:
                return redirect("/infoentrenador/?novalido")
               
    
    
    
    
    
    return render(request,"infoentrenador/contactos.html",{"formulario":formulario_entrenador})
