from django.shortcuts import (
    render,
    get_object_or_404,
)

from .models import (
    Order,
    OrderItem,
)
from book.models import Book

# Create your views here.
def place_order(request, payment_method):
    template_name = 'order/complete.html'
    context ={}

    item_list = request.session.get('key_list', [])
    books = []
    order_value = 0

    # for i in range(0, len(item_list)):
    for iter_book in item_list:
        book = get_object_or_404(
            Book,
            id=iter_book,
        )
        order_value += book.sale_price
        books.append(book)

    if not request.user.is_authenticated or not hasattr(request.user, 'customer'):
        return redirect('/u/?next=' + request.path)
    else:
        order = Order(
            customer=request.user.customer,
            total=order_value,
            payment_method=payment_method,
        )
        order.save()
        for book in books:
            order_item = OrderItem(
                item=book.title,
                price=book.sale_price,
                vendor=book.vendor,
                order=order,
            )
            order_item.save()

        request.session['key_list'] = []
        return render(request, template_name, context)

def order_details(request, id):
    template_name = 'order/details.html'
    context = {}

    order = get_object_or_404(
        Order,
        id=id,
    )

    order_items = OrderItem.objects.all().filter(
        order=order,
    )

    context.update({
        'order': order,
        'order_items': order_items,
    })

    return render(request, template_name, context)
