from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login
from django.views import generic
from django.urls import reverse_lazy
from .models import  *
from .filters import *
from django.contrib.auth.mixins import LoginRequiredMixin


def profile(request):
    context ={

        'perfiluser' : Programador.objects.filter(usuario = request.user)

    }
    return render(request, 'profile/profile.html', context)
   

def menu(request):
    context = {
        'snippet' : SnippeFilter(request.GET, queryset=Snippet.objects.filter(privacidad = False)),
        "perfiluser" : Programador.objects.filter(usuario = request.user)

    }
    return render(request, "componentes/menu.html", context)



def missnippets(request):
    context = {
        'snippet' : Snippet.objects.filter(usuario = request.user)

    }
    return render(request, "snippets_functions/tabla_snippet.html", context)






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
    template_name = 'snippets_functions/editar.html'
    form_class = FormSnippet
    success_url = reverse_lazy('codeuser:missnippets')

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial={'usuario': request.user })

        return render(request, self.template_name, {'form': form
        })

    

class EditarSnippet(LoginRequiredMixin, generic.UpdateView):
    template_name = 'snippets_functions/editar.html'
    model = Snippet
    form_class = FormSnippet
    success_url = reverse_lazy('codeuser:missnippets')


class VerSnippet(LoginRequiredMixin, generic.DetailView):
    template_name = 'snippets_functions/ver.html'
    model = Snippet
    

class  EliminarSnippet(LoginRequiredMixin, generic.DeleteView):
    template_name = 'snippets_functions/eliminar.html'
    model = Snippet
    success_url = reverse_lazy('codeuser:missnippets')

