from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from products.models import Product
from .forms import ReviewForm


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'product': product
        }
    return render(request, 'reviews/add_review.html', context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    if request.user == review.user or request.user.is_superuser:
        if request.method == 'POST':
            if request.method == 'POST':
                form = ReviewForm(request.POST, instance=review)
                if form.is_valid():
                    form.save()
                    return redirect('product_detail', product_id=review.product.id)
        else:
            form = ReviewForm(instance=review)
            context = {
                'form': form,
                'review': review
                }
        return render(request, 'reviews/edit_review.html', context)
    else:
        messages.error(request, "You are not authorised to edit a review")
        return redirect(reverse('product_detail', product_id=review.product.id))


@login_required
def delete_review(request, review_id):

    review = get_object_or_404(Review, id=review_id)
    if request.user == review.user or request.user.is_superuser:
        review.delete()
        return redirect('product_detail', product_id=review.product.id)
    else:
        messages.error(request, "You are not authorised to edit a review")
        return redirect(reverse('product_detail', product_id=review.product.id))
