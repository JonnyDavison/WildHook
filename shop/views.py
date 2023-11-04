from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, View
from .models import Item, OrderItem, Order
from django.utils import timezone
from django.contrib import messages
from .forms import CheckoutForm

class ProductView(DetailView):
    model = Item
    shop_template = 'shop/item_detail.html'


class OrderSummary(LoginRequiredMixin, View):
    def get(self, args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order,
            }
            return render(self.request,'shop/order_summary.html', context)
        
        except ObjectDoesNotExist:
            messages.error(self.request, "No active order found")
            return redirect('/')


def item_list(request):

    items = Item.objects.all()
    shop = 'shop/item_list.html'

    context = {
        'items': items
    }
    return render(request, shop, context)

@login_required
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
            messages.info(request, "The item quantity was updated.")
            return redirect('shop:order_summary')

        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect('shop:order_summary')

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,
                                     ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "The item quantity was updated")
    return redirect('shop:order_summary')

@login_required
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
            messages.info(request, "This item was removed from your cart")
            return redirect("shop:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('shop:product', slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('shop:product', slug=slug)

@login_required
def remove_single_item_from_cart(request, slug):
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
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "Item quantity updated")
            return redirect("shop:order_summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect('shop:product', slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect('shop:product', slug=slug)


class CheckoutView(View):
    def get(self, *args, **kwargs):
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }
            return render(self.request, "shop/checkout.html", context)
            
    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        print(self.request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            print("FORM VALID")
            return redirect('shop:checkout')
        messages.warning(self.request, "FAILED CHECKOUT")
        return redirect('shop:checkout')
          