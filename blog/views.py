from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm


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
    meta_keywords = post.meta_keywords 
    meta_description = post.meta_description 
    queryset = Post.objects.filter()
    
    context = {
        'post': post,
        'meta_keywords': meta_keywords,
        'meta_description': meta_description,
        
        }
    return render(request, 'blog/post_detail.html', context)

@login_required
def create_post(request):
    """View to create a new blog post."""
    if not request.user.is_superuser:
        return redirect('post_list')  # Redirect if user is not a superuser
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if not request.user.is_superuser:
        # If not a superuser, return a message & redirect
        messages.error(request, "You do not have permission to access this page.")
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post(request, slug):
    """View to delete an existing blog post."""
    post = get_object_or_404(Post, slug=slug)
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('post_detail', slug=post.slug)
    post.delete()
    messages.success(request, 'Post deleted.')
    return redirect('post_list')
