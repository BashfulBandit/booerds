# Define Django things here.
from django.shortcuts import (
    render,
)

from book.models import Book

# Create your views here.
def home(request):
    # Define the template and an empty context dict.
    template_name = 'bookstore/home.html'
    context = {}

    # Get some books
    featured_books = Book.objects.all().filter(featured=True)

    # Add the books the context dict.
    context.update({
        'featured_books': featured_books,
    })
    # Render the reponse.
    return render(request, template_name, context)
