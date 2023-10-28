from django.shortcuts import render
from django.core.paginator import Paginator

from .models import BookData

# Create your views here.
def home_view(request, *args, **kwargs):
    book_list = BookData.objects.all()
    paginator = Paginator(book_list, 5)  # Show 5 contacts per page.
    
    page_number = request.GET.get("page")
    
    book_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(number=page_number) # add ellipsis

    my_context = {
        "book_list": book_obj,
        "page_range": page_range,
        "site_title": "Home"
    }
    return render(request, "home.html", my_context) # return an html template