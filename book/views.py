from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from .models import Book
from .forms import (
    BookCreationForm,
    BookChangeForm,
)

def delete_book(request, book_id):
    # Define the template and an empty context dict.
    template_name = 'book/delete_book.html'
    context = {}

    # Check to make sure the request user is logged in and is a Vendor.
    if not request.user.is_authenticated and not hasattr(request.user, 'vendor'):
        return redirect('users:user_login')
    # Get the Book from the DB.
    book = Book.objects.get(id=book_id)
    # Make sure the request user owns the Book.
    if book.vendor.id == request.user.vendor.id:
        book.delete()
        # Redirect to the user profile.
        return redirect('users:profile', id=request.user.id)
    # If the user doesn't own the Book then redirect to home page.
    else:
        return redirect('bookstore:home')


def edit_book(request, book_id):
    # Define the template and an empty context dict.
    template_name = 'book/edit_book.html'
    context = {}

    # Check to make sure the request user is logged in and is a Vendor.
    if not request.user.is_authenticated and not hasattr(request.user, 'vendor'):
        return redirect('users:user_login')
    # request is a POST.
    elif request.method == 'POST':
        # Get the Book from the DB.
        book = Book.objects.get(id=book_id)
        # Get the data from the form.
        book_form = BookChangeForm(
            request.POST,
            request.FILES,
            instance=book,
        )
        # Check if the form is valid.
        if book_form.is_valid():
            # Save to DB.
            book_form.save()
            # Redirect to user profile.
            return redirect('users:profile', id=request.user.id)
        # Form isn't valid.
        else:
            # Put the form back in the context dict.
            context.update({
                'book_form': book_form,
            })
            # Render the template with the context.
            return render(request, template_name, context)
    else:
        # Get the Book from the DB we are editing.
        book = Book.objects.get(id=book_id)
        # Make the Form from the Book instance from the DB.
        book_form = BookChangeForm(
            instance=book,
        )
        context.update({
            'book_form': book_form,
        })
        # Render the template with the context dict.
        return render(request, template_name, context)

def add_book(request, vendor_id):
    # Define the template and an empty context dict.
    template_name = 'book/add_book.html'
    context = {}

    # Check whether the user is logged in and also a Vendor.
    if not request.user.is_authenticated or not hasattr(request.user, 'vendor'):
        return redirect('bookstore:home')
    # User is logged in and is a Vendor, so check if request is a POST.
    elif request.method == 'POST':
        # Get the form from the request.
        book_form = BookCreationForm(
            request.POST,
            request.FILES
        )
        # Check if the form is valid.
        if book_form.is_valid():
            book = book_form.save()
            book.vendor = request.user.vendor
            book.save()
            # Redirect Vendor to profile page.
            return redirect('users:profile', id=request.user.id)
        # Form is not valid. Return it to user with errors.
        else:
            context.update({
                'book_form': book_form,
            })
            return render(request, template_name, context)
    # GET request.
    else:
        # Initialize an empty Book form.
        book_form = BookCreationForm()
        # Put form in context dict.
        context.update({
            'book_form': book_form,
        })
        # Render template with the contect dict.
        return render(request, template_name, context)

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
