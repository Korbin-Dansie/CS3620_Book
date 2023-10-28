from django.shortcuts import render
from rest_framework import viewsets

from .models import BookData

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "site_title": "Home"
    }
    return render(request, "home.html", my_context) # return an html template