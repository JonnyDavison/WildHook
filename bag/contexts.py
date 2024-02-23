from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    """ bag Context processor allows bag contents to be available globally """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    saving = 0

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        offer_price = product.offer_price

        if offer_price is not None:
            sub_total = offer_price * quantity
            saving = (product.price * quantity) - (product.offer_price * quantity)
        else:
            sub_total = total

        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'offer_price': offer_price,
            'sub_total': sub_total,
            'saving': saving
        })

    if total < settings.FREE_DELIVERY:
        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery': settings.FREE_DELIVERY,
        'grand_total': grand_total,
    }

    return context
