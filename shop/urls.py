from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import (
    ProductView,
    add_to_cart,
    )

app_name = 'shop'

urlpatterns = [
    path('item_list', views.item_list, name='item_list'),
    path('product/<slug>/', ProductView.as_view(), name='product')
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart')

]
