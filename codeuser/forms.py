from django import forms 
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import UserCode

class Createuser(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = UserCode
        fields = ('email','username')
       

    def clean_password(self):
        password1 = self.cleaned_data.get(password1)
        password2 = self.cleaned_data.get(password2)

        if password1 and password2 != password1 and password2:
            raise ValueError('Password or username not valid')
    
        return password2

    def save(self, commit=True):
        usuario = super(Createuser, self).save(commit=False)
        usuario.set_password(self.clean_password)
        usuario.is_active = True
        if commit:
            usuario.save()

        
        return usuario
 
class NewUserForm(forms.ModelForm): #Conductor
    #Nos ayuda a crear un conductor nuevo desde la página del admin
    class Meta:
        model = UserCode
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
    model = UserCode
 
class Users_Form(UserCreationForm):
    #Con esta línea podemos obtener el correo
    email  = forms.CharField(max_length=64)
    

# class LoginAdminForm(forms.Form):
#     username_admin = forms.CharField(widget=forms.TextInput())
#     password_admin = forms.CharField(widget=forms.PasswordInput())


