from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from .models import  *
from .filters import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import requests 
import json

def profile(request):
    context ={

        'perfiluser' : Programador.objects.filter(usuario = request.user)

    }
    return render(request, "nuevo_template/user.html", context)
   


def generate_request(url):
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()


def menu(request):


    response = generate_request('http://localhost:8000/Url_code_saved/Snippet/')
    data_string = json.dumps(response)
    decoded = json.loads(data_string)



    context = {
        'snippet' : Snippet.objects.filter(privacidad = False),
        "perfiluser" : Programador.objects.filter(usuario = request.user),
        'code_saved' :  decoded,
        

    }
    return render(request, "nuevo_template/dashboard.html", context)



def missnippets(request):
    context = {
        'snippet' : Snippet.objects.filter(usuario = request.user)

    }
    return render(request, "nuevo_template/tables.html", context)






############################### CRUD PROFILE  ###############################
class Crearprofile(generic.CreateView):
    template_name = 'profile/crear_profile.html'
    form_class = FormProgramador
    success_url = reverse_lazy('codeuser:profile')

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial={'usuario': request.user })

        return render(request, self.template_name, {'form': form
        })



class Editarprofile(LoginRequiredMixin, generic.UpdateView):
    template_name = 'profile/editar_profile.html'
    model = Programador
    form_class = FormProgramador
    success_url = reverse_lazy('codeuser:profile')


############################### CRUD SNIPPET  ###############################



class CrearSnippet(generic.CreateView):
    template_name = 'nuevo_template/typography.html'
    form_class = FormSnippetEdit
    success_url = reverse_lazy('codeuser:missnippets')


    def get(self, request, *args, **kwargs):

        form = self.form_class(initial={'usuario': request.user })


        return render(request, self.template_name, {'form': form
        })

    

class EditarSnippet(LoginRequiredMixin, generic.UpdateView):
    template_name = 'snippets_functions/editar.html'
    model = Snippet
    form_class = FormSnippetEdit
    success_url = reverse_lazy('codeuser:missnippets')


class VerSnippet(LoginRequiredMixin, generic.DetailView):
    template_name = 'snippets_functions/ver.html'
    model = Snippet
    

class  EliminarSnippet(LoginRequiredMixin, generic.DeleteView):
    template_name = 'snippets_functions/eliminar.html'
    model = Snippet
    success_url = reverse_lazy('codeuser:missnippets')

