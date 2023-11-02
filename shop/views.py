from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Item, OrderItem, Order
from django.utils import timezone
from django.contrib import messages


class ProductView(DetailView):
    model = Item
    shop_template = 'shop/item_detail.html'


def item_list(request):

    items = Item.objects.all()
    shop = 'shop/item_list.html'

    context = {
        'items': items
    }
    return render(request, shop, context)


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_query = Order.objects.filter(user=request.user, ordered=False)
    if order_query.exists():
        order = order_query[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,
                                     ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect('shop:product', slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_query = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_query.exists():
        order = order_query[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("shop:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('shop:product', slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('shop:product', slug=slug)
