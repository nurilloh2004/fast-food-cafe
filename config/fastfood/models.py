from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from .utils import *
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
# Create your models here.

class User(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(null=True)
    release_date = models.DateField(default=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        password = self.password
        self.set_password(password)
        print("sending sms to email")
        send_mail(
            "Created user",
            "Test message",
            EMAIL_HOST_USER,
            ["alharamin1004 @gmail.com"],
            fail_silently=False
        )
        return super(User,self).save(*args, **kwargs)




class Product(models.Model):
    name = models.CharField(max_length=65)
    price = models.IntegerField(max_length=65)
    amount = models.IntegerField(max_length=65)
    slug = models.SlugField()
    date = models.DateField()

    def __str__(self) -> str:
        return self.name

class Customers(models.Model):
    customer = models.OneToOneField(Customer)
    


