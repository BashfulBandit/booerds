from django.shortcuts import (
    render,
    get_object_or_404,
)

from book.models import Book

# Create your views here.

def cart(request, id):
    
    url_name = request.get_host()
    
    url_name += "/cart/show_cart/"
    
    template_name = 'cart/pre_cart.html'
    
    item_list = request.session.get('key_list', [])
        
    item_list.append(id)
    
    request.session['key_list'] = item_list
    
    request.session.modified = True
    
    return render(request, template_name, {'url_name': url_name})

def show_cart(request):
     
    context = {}
    
    template_name = 'cart/cart.html'
    
    item_list = request.session.get('key_list', [])
    
    book_list = []
    
    for i in range(0, len(item_list)):
        
        book_list.append(get_object_or_404(Book, id = item_list[i]))
    
    # Add the book to the context dict.
    context.update({
        'cart': book_list,
    })
         
    return render(request, template_name, context)

def delete(request,id):

    item_list = request.session.get('key_list', [])
    
    for i in range(0, len(item_list)):
            
        if(id == item_list[i]):
                
            del item_list[i]
            break
    
    request.session['key_list'] = item_list
    
    request.session.modified = True

    show_cart(request)





