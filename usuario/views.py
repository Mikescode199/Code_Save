from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, UserCreationForm, Users_Form, NewUserForm
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from .models import  Usuario
# Create your views here.


def registro_user(request):
    message = 'NOt LOgin'
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user = request.POST['username']
            password = request.POST['password']
            print(user, password)
            user = authenticate(username= user, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('usuario:profile')
                    message = 'user Loged'
                   
                else:
                    message = 'User NO ACTIVE'
            else:
                message = 'User or password incorracte'
        context ={
        'form': form, 
        'message': message
        }
    context ={
        'form': form,
        'message': message
    }
    return render(request, 'login/login.html', context)

class CrearUsuario(generic.FormView):
    template_name = 'register/register.html'
    form_class = Users_Form
    success_url = reverse_lazy('usuario:registro_user')

    def form_valid(self, form):
        user = form.save()
        return super(CrearUsuario, self).form_valid(form)

def profile(request):
    model = Usuario
    context ={
       
    }
    return render(request, 'profile/profile.html', context)





