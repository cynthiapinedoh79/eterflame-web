from django.contrib import admin
from .models import AffiliateLink


@admin.register(AffiliateLink)
class AffiliateLinkAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'channel', 'commission', 'featured', 'active', 'order']
    list_filter   = ['category', 'channel', 'featured', 'active']
    list_editable = ['order', 'featured', 'active']
    search_fields = ['name', 'description']
