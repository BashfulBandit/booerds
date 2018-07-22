from django.shortcuts import (
    render,
    get_object_or_404,
)

from .models import Order

from book.models import Book

from .models import Order_Detail


# Create your views here.

def place(request):
    
    template_name = 'order/complete.html'
    
    item_list = request.session.get('key_list', [])

    book_list = []
    
    order_value = 0

    for i in range(0, len(item_list)):
        temp_book = get_object_or_404(Book, id=item_list[i])
        order_value += temp_book.sale_price
        book_list.append(temp_book)
        
    order_row = Order(customer_id = 1, order_total = order_value)
    order_row.save()
    for i in range(0, len(book_list)):
        order_detail_row = Order_Detail(book_id = book_list[i].id, vendor_id = 0, order = order_row)
        order_detail_row.save()
    
    return render(request, template_name,{})
    
    