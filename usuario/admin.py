from django.contrib import admin

# Register your models here.
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    Lista_show = [
        'id',
    ]