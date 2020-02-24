from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin


app_name = 'codigo'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('savecode/', views.savecode, name='savecode'),

]
