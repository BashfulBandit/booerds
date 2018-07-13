# Define Django things here.
from django.shortcuts import (
    render,
)

# Create your views here.
def home(request):
    # Define the template and an empty context dict.
    template_name = 'bookstore/home.html'
    context = {}

    # Get some books

    # Add the books the context dict.

    # Render the reponse.
    return render(request, template_name, context)
