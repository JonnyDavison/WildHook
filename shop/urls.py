from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import item_list

app_name = 'shop'

urlpatterns = [
    path('', item_list, name='item-list')
]
