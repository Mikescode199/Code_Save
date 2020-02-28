from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save


# Create your models here.
# User model

class MyaccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('You must have an email')

        if not username:
            raise ValueError('You must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            
        )

        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            password = password,
            username = username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user



class UserCode(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(  max_length=60, unique=True) 
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_joined = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    birth = models.CharField(max_length=30)
    profetion = models.CharField(max_length=30)
    aboutme = models.TextField()
    image_user = models.ImageField()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyaccountManager()

# def  create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserCode.objects.create(user=kwargs['instance'])

# post_save.connect(create_profile, sender = User)
