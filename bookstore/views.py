# Define Django things here.
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth import (
    logout,
    login,
    authenticate,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm

# Define our app items here.
from book.models import Book
from users.models import (
    Customer,
    Vendor,
)
from users.forms import (
    MyUserCreationForm,
    CustomerCreationForm,
    VendorCreationForm,
)

# Create your views here.
def user_login(request):
    template_name = 'bookstore/forms.html'
    context = {}

    if request.user.is_authenticated:
        return redirect('bookstore:profile', id=request.user.id)
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('bookstore:profile', id=user.id)
    else:
        form = AuthenticationForm()
        context.update({
            'form_name': 'Login',
            'form': form,
        })
        return render(request, template_name, context)

def user_logout(request):
    logout(request)
    return redirect('bookstore:home')

def register(request):
    return redirect('bookstore:customer_register')

@transaction.atomic
def customer_register(request):
    template_name = 'bookstore/forms.html'
    context = {}

    if request.user.is_authenticated:
            return redirect('bookstore:profile', id=request.user.id)
    elif request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        customer_form = CustomerCreationForm(request.POST)

        if user_form.is_valid() and customer_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data['username']
            raw_password = user_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=raw_password)
            print(user.id)
            print(customer_form)
            customer_form.cleaned_data['user'] = user.id
            print(customer_form)
            customer_form.save()
            if user is not None:
                login(request, user)
                return redirect('bookstore:profile', id=user.id)
    else:
        user_form = MyUserCreationForm()
        customer_form = CustomerCreationForm()

        context.update({
            'form_name': 'Customer Registration Form',
            'user_form': user_form,
            'form': customer_form,
        })
        return render(request, template_name, context)

def vendor_register(request):
    template_name = 'bookstore/forms.html'
    context = {}

    if request.user.is_authenticated:
        return redirect('bookstore:profile', id=request.user.id)
    elif request.method == 'POST':
        user_form = MyUserCreationForm(request.POST)
        vendor_form = VendorCreationForm(request.POST)

        if user_form.is_valid() and vendor_form.is_valid():
            user_form.save()
            vendor_form.save()
            username = user_form.cleaned_data['username']
            raw_password = user_form.cleaned_data['password1']
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
            return redirect('bookstore:profile', id=user.id)
    else:
        user_form = MyUserCreationForm()
        vendor_form = VendorCreationForm()

        context.update({
            'form_name': 'Vendor Registration Form',
            'user_form': user_form,
            'form': vendor_form,
        })
        return render(request, template_name, context)

@login_required
def profile(request, id):
    # Define the template and en empty context dict.
    template_name = 'bookstore/profile.html'
    context = {}

    # Get the User object which has been request or 404
    user = get_object_or_404(User, id=id)

    # If the request user is not the same as the user we
    # got from the DB then redirect to home page.
    # TODO Make an error page to redirect them to.
    # if request.user.id == user.id:
    #     return redirect('/')
    # else:
    # Append the user to the context dict.
    context.update({
        'user': user,
    })

    # Render the reponse.
    return render(request, template_name, context)

def list(request):
    # Define the template and an empty context dict.
    template_name = 'bookstore/list.html'
    context = {}
    
    #Extract information from the request object.
    
    text = request.GET["search_text"]
    
    category = request.GET["category"]
        
    #Creating the list of display items.
    display_results = []

    #These conditions represent the filtering. 
    
    if(category == "title"):
            
        display_results = Book.objects.all().filter(title__contains=text)
                     
    elif(category == "author"):
        display_results = Book.objects.all().filter(author__contains=text)
                     
    elif(category == "isbn"):
        display_results = Book.objects.all().filter(ISBN=text)
    
    else:
        display_results = Book.objects.all().filter(subject=text)
    
    # Append the books into the context dict to send to the template.
    context.update({
        'books': display_results,
    })
    # Render the response.
    return render(request, template_name, context)

def details(request, id):
    # Define the template and an empty context dict.
    template_name = 'bookstore/details.html'
    context = {}

    # Check to see if there is an Book object in the DB with the id.
    book = get_object_or_404(Book, id=id)

    # Add the book to the context dict.
    context.update({
        'book': book,
    })

    # Render the reponse.
    return render(request, template_name, context)

def home(request):
    # Define the template and an empty context dict.
    template_name = 'bookstore/home.html'
    context = {}

    # Get some books

    # Add the books the context dict.

    # Render the reponse.
    return render(request, template_name, context)
