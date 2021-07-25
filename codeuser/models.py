from django.db import models
from django.contrib.auth.models import User




class Lenguaje_programacion(models.Model):
    nombre = models.CharField(max_length = 30 )

    def __str__(self):
        return '{}'.format(self.nombre)


class Programador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 30 )
    apellidos  = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    correo =  models.EmailField(blank = False)
    direccion  = models.CharField(max_length=30)
    repositorio_gitlab = models.URLField(blank = True)
    repositorio_github = models.URLField(models.URLField(blank = True))
    lenguajes_programacion = models.ManyToManyField(Lenguaje_programacion)
    imagen_perfil  = models.ImageField(upload_to='Imagenes', default = "anonimo.png")
    aboutme = models.TextField(default="I'm so dope")

    def __str__(self):
        return '{}'.format(self.nombre)


class Categoria(models.Model):
    categoria = models.CharField(max_length = 20 )

    def __str__(self):
        return '{}'.format(self.categoria)



class Snippet(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    lenguajeProgramacion = models.ForeignKey(Lenguaje_programacion, on_delete=models.CASCADE)
    codigo_foto = models.ImageField(blank = True, upload_to='media/images')
    codigo_texto = models.TextField(blank = True)
    informacion_codigo  = models.TextField(blank = True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    privacidad = models.BooleanField(default = False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.informacion_codigo)
