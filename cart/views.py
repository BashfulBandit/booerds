from django.shortcuts import (
    render,
    redirect,
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
    
    order_value = 0

    for i in range(0, len(item_list)):
        temp_book = get_object_or_404(Book, id=item_list[i])
        order_value += temp_book.sale_price
        book_list.append(temp_book)
    
    print(order_value)
    
    # Add the book to the context dict.
    context.update({
        'cart': book_list,
        'order_total': order_value,
    })

    return render(request, template_name, context)

def delete_from_cart(request, id):
    item_list = request.session.get('key_list', [])

    for i in range(0, len(item_list)):
        if id == item_list[i]:
            del item_list[i]
            break

    request.session['key_list'] = item_list
    request.session.modified = True

    return redirect('cart:show_cart')

def checkout(request):
    
    template_name = 'cart/checkout.html'
    context = {}
    
    item_list = request.session.get('key_list', [])
    
    book_count = len(item_list)
        
    book_list = []
    
    order_value = 0

    for i in range(0, len(item_list)):
        temp_book = get_object_or_404(Book, id=item_list[i])
        order_value += temp_book.sale_price
        book_list.append(temp_book)
    
    User_Name = request.user.id
    
    context.update({
        'cart': book_list,
        'order_total': order_value,
        'User_Name': User_Name,
        'Book_Count': book_count,
    })
    
    return render(request, template_name, context)




