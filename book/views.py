from django.shortcuts import render

from .models import Book

def book_list(request):
    
    books = Book.objects
    return render(request, 'book/book_list.html', {'books':books})

# Create your views here.
