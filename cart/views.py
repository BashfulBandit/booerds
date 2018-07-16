from django.shortcuts import (
    render,
    get_object_or_404,
)

from book.models import Book

# Create your views here.

def cart(request, id):
    
    template_name = 'cart/pre_cart.html'
    
    item_list = request.session.get('key_list', [])
        
    item_list.append(id)
    
    print(item_list)
    
    request.session['key_list'] = item_list
    
    print(request.session.session_key)
    
    request.session.modified = True
    
    return render(request, template_name, {})

def show_cart(request,id):
    
    print("Hey I am here")
    
    context = {}
    
    template_name = 'cart/cart.html'
    
    item_list = request.session.get('key_list', [])
    
    print(request.user.username)
    
    print(request.session.session_key)
    
    book_list = []
    
    for i in range(0, len(item_list)):
        
        book_list.append(get_object_or_404(Book, id = item_list[i]))
    
    print(len(item_list))
    
    print(book_list)
    
    # Add the book to the context dict.
    context.update({
        'cart': book_list,
    })
         
    return render(request, template_name, context)

