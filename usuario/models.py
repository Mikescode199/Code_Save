from django.db import models

# Create your models here.
# User model
class Usuario(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    birth = models.CharField(max_length=30)
    profetion = models.CharField(max_length=30)
    aboutme = models.TextField()
    image_user = models.ImageField()