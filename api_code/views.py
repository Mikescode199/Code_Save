from django.shortcuts import render
from rest_framework import viewsets
from .serializer import SnippetSerializer
from codeuser.models import Snippet

# Create your views here.
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

#Create token api 
#http://www.django-rest-framework.org/tutorial/1-serialization/