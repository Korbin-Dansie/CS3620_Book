from django.shortcuts import render
from rest_framework import viewsets

from .models import BookData

# Create your views here.
def home_view(request, *args, **kwargs):
    book_list = BookData.objects.all()

    my_context = {
        "book_list": book_list,
        "site_title": "Home"
    }
    return render(request, "home.html", my_context) # return an html template