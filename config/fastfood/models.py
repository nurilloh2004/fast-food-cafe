from django.db import models
from django.contrib.auth.models import User
from .utils import *
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(null=True)
    release_date = models.DateField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=65)
    price = models.IntegerField(max_length=65)
    amount = models.IntegerField(max_length=65)
    slug = models.SlugField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.name


