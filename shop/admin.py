from django.contrib import admin
from .models import Product, CommissionRequest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available', 'featured', 'created_on')
    list_filter = ('category', 'is_available', 'featured')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(CommissionRequest)
class CommissionRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'occasion', 'language', 'submitted_on', 'read')
    list_filter = ('occasion', 'language', 'read')
    readonly_fields = ('submitted_on',)
