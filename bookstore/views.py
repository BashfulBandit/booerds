from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'bookstore/home.html'

    context = {

    }
    return render(request, template_name, context)

def list(request):
    template_name = 'bookstore/list.html'

    context = {

    }
    return render(request, template_name, context)

def details(request, slug):
    template_name = 'bookstore/details.html'

    context = {
        'slug': slug,
    }
    return render(request, template_name, context)
