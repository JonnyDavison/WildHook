from django.contrib import admin
from .models import Order, OrderLineItem
from django.contrib.admin.models import LogEntry

class OrderLineItemAdminInline(admin.TabularInline):
    """ OrderlineItem registration """
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """ Register the model in the admin and give access to OrderLineItemAdminInline """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 'stripe_pid',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'delivery_cost',
              'order_total', 'grand_total', 'original_bag', 'stripe_pid',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost',
                    'grand_total',)

    ordering = ('-date',)


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """ Allow logs to be visible in the admin panel for testing """
    list_display = ['action_time', 'user', 'content_type',
                    'object_id', 'object_repr', 'action_flag', 'change_message']
    list_filter = ['action_time', 'user']
    search_fields = ['user__username', 'change_message']


admin.site.register(Order, OrderAdmin)
