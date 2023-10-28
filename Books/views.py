from django.shortcuts import render
from rest_framework import viewsets

from .models import BookData

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html") # return an html template