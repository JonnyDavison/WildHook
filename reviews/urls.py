# reviews/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('reviews/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('reviews/<int:review_id>/delete/', views.delete_review, name='delete_review'),
]
