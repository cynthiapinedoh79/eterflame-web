from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'division', 'rating_display', 'is_featured', 'is_active', 'order')
    list_filter = ('division', 'rating', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active', 'order')
    search_fields = ('author_name', 'author_role', 'quote')
    
    fieldsets = (
        ('Division', {
            'fields': ('division',)
        }),
        ('Testimonial', {
            'fields': ('quote', 'rating')
        }),
        ('Author', {
            'fields': ('author_name', 'author_role', 'author_company')
        }),
        ('Display options', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )
    
    @admin.display(description='Rating')
    def rating_display(self, obj):
        return obj.stars
