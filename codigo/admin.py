from django.contrib import admin
from .models import Codigo

# Register your models here.
@admin.register(Codigo)
class CodigoAdmin(admin.ModelAdmin):
    Lista_show = [
        'id',
    ]