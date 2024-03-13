from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'publication_date')
    list_filter = ('author', 'publication_date')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
