from django.db import models
from django.contrib.auth.models import User
from .utils import *
# Create your models here.

class User(DataInfo):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(null=True)

    def __str__(self):
        return self.name
