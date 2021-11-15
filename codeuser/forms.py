from django import forms
from django.forms import widgets 
from .models import *


class FormLenguaje_programacion(forms.ModelForm):
    class Meta:
        model = Lenguaje_programacion
        fields = "__all__"



    


class FormProgramador(forms.ModelForm):
    class Meta:
        model = Programador
        fields = [
            'usuario',
            'nombre',
            'apellidos',
            'telefono',
            'correo',
            'direccion',
            'repositorio_gitlab',
            'repositorio_github',
            'lenguajes_programacion',
            'imagen_perfil',
            'aboutme',
        ]

        labels = {
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'telefono': 'Telefono',
            'correo': 'Correo',
            'direccion': 'Direccion',
            'repositorio_gitlab': 'Repositorio Gitlab',
            'repositorio_github': 'Repositorio Github',
            'lenguajes_programacion': 'Lenguajes de programacion',
            'imagen_perfil': 'Imagen de perfil',
            'aboutme': 'Acerca de mi',
        }

        widgets = {
            'usuario' : forms.HiddenInput(),
            'nombre': widgets.TextInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),      
            'apellidos': widgets.TextInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),
            'telefono': widgets.TextInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),
            'correo': widgets.EmailInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),
            'direccion': forms.TextInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),
            'repositorio_gitlab': forms.URLInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),
            'repositorio_github': forms.URLInput(attrs={'class':"form-control", 'id':"exampleFormControlInput1"}),
            'lenguajes_programacion': forms.SelectMultiple(attrs={'class':"form-control", 'id':"exampleFormControlSelect1"}),
            'imagen_perfil':forms.FileInput(attrs={'class':"form-control-file", 'id':"exampleFormControlFile1"}),
            'aboutme':  forms.Textarea(attrs={'class':"form-control", 'id':"exampleFormControlTextarea1"}),

        }



class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = "__all__"

class FormSnippetEdit(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
        'usuario',
        'lenguajeProgramacion',
        'codigo_foto',
        'codigo_texto' ,
        'informacion_codigo',
        'categoria',
        'privacidad']

        label = {
            'lenguajeProgramacion': 'Lenguaje de programacion',
            'codigo_foto': 'Codigo de foto',
            'codigo_texto': 'Codigo de texto',
            'informacion_codigo': 'Informacion del codigo',
            'categoria': 'Categoria',
            'privacidad': 'Privacidad',
        }

        widgets = {
            'usuario': forms.HiddenInput(),
            'lenguajeProgramacion': forms.Select(attrs={'class':"form-control", 'id':"exampleFormControlSelect1"}),
            'codigo_foto': forms.FileInput(attrs={'class':"form-control-file", 'id':"exampleFormControlFile1", 'placeholder':"Seleccionar archivo"}),
            'codigo_texto': forms.Textarea(attrs={'class':"form-control", 'id':"exampleFormControlTextarea1", 'placeholder':"codigo_texto"}),
            'informacion_codigo': forms.Textarea(attrs={'class':"form-control", 'id':"exampleFormControlTextarea1", 'placeholder':"informacion_codigo"}),
            'categoria': forms.Select(attrs={'class':"form-control", 'id':"exampleFormControlSelect1"}),
            'privacidad': forms.CheckboxInput(attrs={'class':"form-control", 'id':"exampleFormControlCheckbox1"}),
        }



