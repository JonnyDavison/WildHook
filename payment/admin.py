from django.contrib import admin
from .models import ShippingInfo, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class PaymentAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_id', 'date',
                       'order_total', 'grand_total')

    fields = ('order_id', 'date', 'name', 'email',
              'phone_number', 'street_address1', 'street_address2',
              'town_or_city', 'county', 'postcode', 'country',
              'order_total', 'grand_total')

    list_display = ('order_id', 'date', 'name',
                    'order_total', 'grand_total')
    
    ordering = ('-date',)


admin.site.register(ShippingInfo, PaymentAdmin)