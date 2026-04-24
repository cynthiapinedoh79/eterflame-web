from django.contrib import admin
from .models import Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ['title', 'series', 'poem', 'created_on', 'active']
    list_filter  = ['series', 'active']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'lyrics']
    raw_id_fields = ['poem']
    fieldsets = (
        ('Info', {
            'fields': ('title', 'slug', 'series', 'poem', 'active', 'cover_image')
        }),
        ('Public video', {
            'description': 'Shown on the song page',
            'fields': ('youtube_url',)
        }),
        ('Streaming platforms', {
            'description': 'Shown on the song page',
            'fields': ('spotify_url', 'apple_music_url',
                       'pandora_url', 'youtube_music_url')
        }),
        ('Social hooks', {
            'description': 'Thumbnails + links shown on the song page',
            'fields': (
                'instagram_url', 'tiktok_url', 'facebook_url',
                'reel_thumbnail',
            )
        }),
        ('PDF download', {
            'fields': ('pdf_price', 'pdf_buy_url')
        }),
        ('Lyrics', {
            'fields': ('lyrics',)
        }),
        ('Production (internal only)', {
            'classes': ('collapse',),
            'description': 'Not shown publicly',
            'fields': ('suno_url',)
        }),
    )
