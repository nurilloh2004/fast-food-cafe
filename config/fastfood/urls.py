import imp
from django.urls import path
from .views import *




urlpatterns = [
    path('' ,HomeView.as_view(), name='home'),
    path('/main' ,HomePageView.as_view(), name='home'),
]