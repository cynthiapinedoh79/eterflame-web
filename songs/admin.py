from django.contrib import admin
from .models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'series', 'poem', 'created_on', 'active']
    list_filter  = ['series', 'active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'lyrics']
    raw_id_fields = ['poem']
