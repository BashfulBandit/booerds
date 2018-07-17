from django.shortcuts import (
    render,
    get_object_or_404,
)

from book.models import Book

# Create your views here.
def add_to_cart(request, id):
    template_name = 'cart/pre_cart.html'
    context = {}

    item_list = request.session.get('key_list', [])
    item_list.append(id)
    request.session['key_list'] = item_list
    request.session.modified = True

    return render(request, template_name, context)

def show_cart(request):
    template_name = 'cart/cart.html'
    context = {}

    item_list = request.session.get('key_list', [])
    book_list = []

    for i in range(0, len(item_list)):
        book_list.append(get_object_or_404(Book, id=item_list[i]))

    # Add the book to the context dict.
    context.update({
        'cart': book_list,
    })

    return render(request, template_name, context)
