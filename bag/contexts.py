from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    """ Context processor allows bag contents to be available globally """

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    saving = 0

    for item_id, item_data in bag.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            price_to_use = product.offer_price if product.offer_price is not None else product.price
            total += item_data * price_to_use
            product_count += item_data
            saving = (product.price * item_data) - (price_to_use * item_data)

            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
                'offer_price': product.offer_price,
                'sub_total': item_data * price_to_use,
                'saving': saving
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                price_to_use = (product.offer_price if product.offer_price is not None
                                else product.price)
                total += quantity * price_to_use
                product_count += quantity
                saving = (product.price * quantity) - (price_to_use * quantity)

                bag_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'offer_price': product.offer_price,
                    'sub_total': quantity * price_to_use,
                    'saving': saving,
                    'size': size
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
