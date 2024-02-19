from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    ProductView,
    OrderSummary,
    CheckoutView,
    # PaymentView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    )

app_name = 'shop'

urlpatterns = [
    path('item_list', views.item_list, name='item_list'),
    path('order_summary', OrderSummary.as_view(), name='order_summary'),
    path('product/<slug>/', ProductView.as_view(), name='product'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove_item_from_cart/<slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    # path('payment/', PaymentView.as_view(), name="PaymentView")
]
