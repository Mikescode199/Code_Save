from django import forms 
from .models import Codigo

class SavecodeForm(forms.ModelForm): #Conductor
    #Nos ayuda a crear un conductor nuevo desde la página del admin
    class Meta:
        model = Codigo
        fields = [
            'tipo_codigo',
            'nombre_etiqueta', 
            'codigo_guardado', 
         ]

        labels = { 
            'tipo_codigo':'Tipo de codigo',
            'nombre_etiqueta':'Lenguaje', 
            'codigo_guardado':'Codigo...',
        }

        widgets = {
            'tipo_codigo' : forms.TextInput(attrs={'class':'form-input'}),
            'nombre_etiqueta' : forms.TextInput(attrs={'class':'form-input'}),
            'codigo_guardado' : forms.TextInput(attrs={'class':'form-input'}),
        }
