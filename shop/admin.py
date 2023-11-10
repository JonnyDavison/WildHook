from django.contrib import admin
from .models import Item, OrderItem, Order

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'price',
        'offer_price',
        'image',
    )
    ordering = ('title',)


class OrderItemAdmin(admin.ModelAdmin):
   list_display = (
        'user',
        'ordered',
        'quantity',
    )
    

class OrderAdmin(admin.ModelAdmin):
   list_display = (
        'user',
        'ordered',
        'ordered_date',
    )
    

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
