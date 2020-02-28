from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, UserCreationForm, Users_Form, NewUserForm, Createuser
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from .models import  UserCode
# Create your views here.

def registro_user(request):
    message = 'NOt LOgin'
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid:
            username = request.POST['username']
            password = request.POST['password']
            print(username, password)
            user = authenticate(username= username, password = password)
            if user is not None:
                if user.is_active:
                    # login(request, user)
                    return redirect('codeuser:profile')

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



class Register(generic.FormView):
    template_name = 'register/register.html'
    form_class = Createuser
    success_url = reverse_lazy('codeuser:registro_user')

    def form_valid(self, form):
        user = form.save()
        return super(Register, self).form_valid(form)


def profile(request):
    context ={

    }
    return render(request, 'profile/profile.html', context)
   


