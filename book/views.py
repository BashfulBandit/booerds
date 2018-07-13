from django.shortcuts import (
    render,
    get_object_or_404,
)

from .models import Book

# Create your views here.
def list(request):
    # Define the template and an empty context dict.
    template_name = 'book/list.html'
    context = {}

    category = ''
    text = ''

    #Extract information from the request object.
    if request.method == 'GET' and 'search_text' in request.GET:
        text = request.GET['search_text']
    if request.method == 'GET' and 'category' in request.GET:
        category = request.GET['category']


    if category == 'title':
        books = Book.objects.all().filter(title__contains=text)
    elif category == 'author':
        books = Book.objects.all().filter(author__contains=text)
    elif category == 'isbn':
        books = Book.objects.all().filter(ISBN=text)
    elif category == 'subject':
        books = Book.objects.all().filter(subject=text)
    else:
        books = Book.objects.all()

    # Append the books into the context dict to send to the template.
    context.update({
        'books': books,
    })
    # Render the response.
    return render(request, template_name, context)

def details(request, id):
    # Define the template and an empty context dict.
    template_name = 'book/details.html'
    context = {}

    # Check to see if there is an Book object in the DB with the id.
    book = get_object_or_404(Book, id=id)

    # Add the book to the context dict.
    context.update({
        'book': book,
    })

    # Render the reponse.
    return render(request, template_name, context)
