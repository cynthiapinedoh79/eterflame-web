from django.contrib import admin
from .models import PortfolioItem


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display  = ['title', 'kicker', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    ordering      = ['order']
