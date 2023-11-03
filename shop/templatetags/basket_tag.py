from django import template
from shop.models import Order

register = template.Library()


@register.filter
def basket_item_count(user):
    if user.is_authenticated:
        q_set = Order.objects.filter(user=user, ordered=False)
        if q_set.exists():
            return q_set[0].items.count()
    return 0