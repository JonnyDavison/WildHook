from django.db import models
from shop.models import Item
import uuid
from django.db.models import Sum
from django.conf import settings


class ShippingInfo(models.Model):
    class Meta:
        verbose_name_plural = 'Shipping Info'

    order_id = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=40, null=False, blank=False)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_id(self):
        return uuid.uuid4().hex.upper()
    
    def update_total(self):
        self.order_total = self.ShippingInfo.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.grand_total = self.order_total
        self.save() 

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = self._generate_order_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_id


class OrderLineItem(models.Model):
    order = models.ForeignKey(ShippingInfo, null=False, blank=False, on_delete=models.CASCADE, related_name='ShippingInfo')
    product = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        offer = self.product.offer_price
        if offer: 
            self.lineitem_total = offer * self.quantity
        else:
            self.lineitem_total = self.product.price * self.quantity
            super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.title} on order {self.order.order_id}'