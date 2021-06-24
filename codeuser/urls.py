from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = 'codeuser'
urlpatterns = [

    path('',
        auth_view.LoginView.as_view(template_name='login/login.html'),
        name='logout_cda'),

    path("menu/", views.menu, name='menu'),
    
    path('profile/', views.profile, name='profile'),

    path('missnippets/', views.missnippets, name='missnippets'),
    
    path("CrearSnippet/", views.CrearSnippet.as_view(), name="CrearSnippet"),
    path("Crearprofile/", views.Crearprofile.as_view(), name="Crearprofile"),
    path("Editarprofile/<int:pk>", views.Editarprofile.as_view(), name="Editarprofile"),
    path("VerSnippet/<int:pk>", views.VerSnippet.as_view(), name="VerSnippet"),
    path("EditarSnippet/<int:pk>", views.EditarSnippet.as_view(), name="EditarSnippet"),
    path("EliminarSnippet/<int:pk>", views.EliminarSnippet.as_view(), name="EliminarSnippet"),
    

    
    
]
