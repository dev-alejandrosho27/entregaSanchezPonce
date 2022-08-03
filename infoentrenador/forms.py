from django import forms 




class FormularioDeEntrenador(forms.Form):
    nombre=forms.CharField(label="Nombre",max_length=30,required=True)
    email=forms.EmailField(label="Email",required=True)
    descripcion=forms.CharField(label="Descripcion",widget=forms.Textarea)
    