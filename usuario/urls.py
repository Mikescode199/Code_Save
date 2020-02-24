from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin


app_name = 'usuario'
urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('', views.registro_user, name='registro_user'), #LogIN user
    path('register/', views.CrearUsuario.as_view(), name='register'),
]
