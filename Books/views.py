from django.shortcuts import render
from django.core.paginator import Paginator

from .models import BookData

# Create your views here.
def home_view(request, *args, **kwargs):
    book_obj = BookData.objects.all() # also a queryset qs

    # Filter dynamicly with a form 
    # Filter based on variables for a book name
    book_name = request.GET.get("book_name")
    if book_name != "" and book_name is not None:
        book_obj = book_obj.filter(name__icontains = book_name)

    paginator = Paginator(book_obj, 5)  # Show 5 contacts per page.
    
    page_number = request.GET.get("page")
    if page_number == "" or page_number == None:
        page_number = 1
    
    book_paginator = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(number=page_number) # add ellipsis

    my_context = {
        "book_list": book_paginator,
        "page_range": page_range,
        "site_title": "Home"
    }
    return render(request, "home.html", my_context) # return an html template