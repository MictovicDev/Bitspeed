from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin)
from .managers import UserManager





class User(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(max_length=250,blank=True, null=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



class ContactDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phonenumber = models.CharField(max_length=26)
    email = models.EmailField(verbose_name='email address',max_length=255)
    linkedid = models.PositiveIntegerField()
    linkedPrecedence = models.CharField(max_length=26)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    # deletedAt = models.DateTimeField(a)
