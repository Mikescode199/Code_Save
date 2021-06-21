from django import forms 
from .models import *

class FormLenguaje_programacion(forms.ModelForm):
    class Meta:
        model = Lenguaje_programacion
        fields = "__all__"
    


class FormProgramador(forms.ModelForm):
    class Meta:
        model = Programador
        fields = "__all__"



class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class FormSnippet(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = "__all__"


