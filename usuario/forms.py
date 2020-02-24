from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class NewUserForm(forms.ModelForm): #Conductor
    #Nos ayuda a crear un conductor nuevo desde la página del admin
    class Meta:
        model = Usuario
        fields = [
            'name',
            'last_name',
            'nickname', 
            'birth', 
            'profetion', 
            'aboutme', 
            'image_user',
         ]
        labels = { 'name'  : 'Name',
            'last_name': 'Last name',
            'nickname': 'Nickname',
            'birth': 'Birth',
            'profetion': 'I am', 
            'aboutme': 'About me',
            'image_user': 'Imagen de usuario', }
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-input'}),
            'last_name' : forms.TextInput(attrs={'class':'form-input'}),
            'nickname' : forms.TextInput(attrs={'class':'form-input'}),
            'profetion' : forms.TextInput(attrs={'class':'form-input'}),
            'aboutme' : forms.TextInput(attrs={'class':'form-input'}),
            'birth' : forms.TextInput(attrs={'class':'form-input', 'type': 'date'}),
            'image_user' : forms.TextInput(attrs={'class':'form-input', 'type': 'image'}),
            
        }


class LoginForm(forms.Form):
    #Con estas lineas de código podemos registrar a un usuario
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

class Users_Form(UserCreationForm):
    #Con esta línea podemos obtener el correo
    email  = forms.CharField(max_length=64)

# class LoginAdminForm(forms.Form):
#     username_admin = forms.CharField(widget=forms.TextInput())
#     password_admin = forms.CharField(widget=forms.PasswordInput())