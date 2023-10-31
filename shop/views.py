from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item


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
