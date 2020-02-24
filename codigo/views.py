from django.shortcuts import render
from django.http import HttpResponse
from .models import Codigo
from django.views import generic
from django.urls import reverse_lazy
from .forms import SavecodeForm

def index(request):
    #Función principal
    context ={
        
    }
    return render(request, 'index.html', context)


def block(request):
    return HttpResponse("This is the block by Mike")

def savecode(request):
    if request.method == 'POST':
        form = SavecodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario:profile')

    else:
        form = SavecodeForm()
        
    return render(request, 'savecode/savecode.html', {'form':form } )