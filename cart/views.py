from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from book.models import Book
from .forms import (
    PaymentChoicesForm,
    PaymentInfoForm,
)

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
    books = []
    order_value = 0

    for book in item_list:
        book = get_object_or_404(
            Book,
            id=book
        )
        order_value += book.sale_price
        books.append(book)

    # Add the book to the context dict.
    context.update({
        'cart': books,
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

def payment_options(request):
    template_name = 'cart/payment_options.html'
    context = {}

    if not request.user.is_authenticated or not hasattr(request.user, 'customer'):
        return redirect('/u/?next=' + request.path)
    elif request.method == 'POST':
        payment_choices_form = PaymentChoicesForm(
            request.POST,
        )
        if payment_choices_form.is_valid():
            payment_choice = payment_choices_form.cleaned_data['payment_options']
            if payment_choice == 'CC':
                item_list = request.session.get('key_list', [])
                book_count = len(item_list)
                books = []
                order_total = 0

                for i in range(0, len(item_list)):
                    book = get_object_or_404(
                        Book,
                        id=item_list[i]
                    )
                    order_total += book.sale_price
                    books.append(book)

                template_name = 'cart/payment_info.html'

                payment_info_form = PaymentInfoForm()

                context.update({
                    'payment_info_form': payment_info_form,
                    'cart': books,
                    'order_total': order_total,
                    'book_count': book_count,
                })
                return render(request, template_name, context)
            elif payment_choice == 'CA':
                return redirect('order:place_order', payment_method='CASH')
            elif payment_choice == 'CH':
                return redirect('order:place_order', payment_method='CHECK')
    else:
        payment_choices_form = PaymentChoicesForm()

        item_list = request.session.get('key_list', [])
        book_count = len(item_list)
        books = []
        order_total = 0

        for i in range(0, len(item_list)):
            book = get_object_or_404(
                Book,
                id=item_list[i]
            )
            order_total += book.sale_price
            books.append(book)

        context.update({
            'payment_choices_form': payment_choices_form,
            'cart': books,
            'order_total': order_total,
            'book_count': book_count,
        })

        return render(request, template_name, context)
