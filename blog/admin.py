from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    1. list_display: Fields to display in the admin list view.
    2. search_fields: Fields to include in the search functionality.
    3. list_filter: Fields to filter the list view.
    4. prepopulated_fields: Automatically populate the slug
    field based on the title.
    5. summernote_fields: Fields that will use the Summernote rich-text editor.
    6. Media: Custom CSS to widen the editor in admin.
    """
    class Media:
        css = {
            'all': ('admin/css/blog_admin.css',)
        }

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


admin.site.register(Comment)
