from django import forms
from .models import *

class Request(forms.Form):
    models = User
    fields = '__all__'