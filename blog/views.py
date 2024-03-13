from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag


def post_list(request):
    """ Display a list of all blog posts """
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
