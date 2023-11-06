from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from shop.models import Item, OrderItem, Order
from .forms import OrderForm

def checkout(request):
    
    order = Order.objects.all()
    total = 0
    print('order in payments/views.py', order)
    if not order:
        messages.error(request, "There's nothing in your bag at the moment")
    order_item = OrderItem.objects.filter(
                user=request.user,
                ordered=False
    )
    
    for item in order_item:
        total += item.get_final_price()
    fee = 5
    if total > 0:
        grand_total = total + fee
    order_form = OrderForm()
    print('orderitems in payments/views.py', order_item)
    template = 'payment/payment.html'
    context = {
        'fee': fee,
        'grand_total': grand_total,
        'order' : order,
        'order_item': order_item,
        'order_form': order_form,
        'total': total,
        'stripe_public_key': 'pk_test_0SMREd7Vdweb1MGRi8S0EycR00JVzSAs5O',
        'client_secret': 'test client secret',
    }
    return render(request, template, context)