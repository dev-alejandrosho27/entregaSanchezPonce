from django.shortcuts import render
from pokeblog.models import Reviews,Tipos
# Create your views here.



def blog(request):
    
    review=Reviews.objects.all()
    return render(request,"pokeblog/blog.html", {"review":review,})
def tipos(request,tipos_id):
    
    
    
    tipo_filtro=Tipos.objects.get(id=tipos_id)
    review=Reviews.objects.filter(tipos=tipo_filtro)
    return render(request, "pokeblog/tipos.html",{"tipo_filtro":tipo_filtro,"review":review})