from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def post_list(request):
    """View to display a list of all blog posts."""
    posts = Post.objects.all()

    context = {
        'posts': posts
        }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    """View to display a detailed view of a blog post."""
    post = get_object_or_404(Post, slug=slug)
    queryset = Post.objects.filter()
    return render(request, 'blog/post_detail.html', {'post': post})
