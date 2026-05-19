from django.contrib import admin
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import Author, Collection, Poem


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin interface for Author model"""
# --- 1. NEW: PREVIEW PHOTO ---
    @admin.display(description="Photo")
    def photo_thumb(self, obj):
        # Check if the photo field has a value
        if obj.photo:
            img_html = (
                '<img src="{}" style="height:40px;border-radius:50%;">'
            )
            return format_html(img_html, obj.photo.url)
        return "—"
    
    # --- 2. UPDATED LIST DISPLAY ---
    list_display = (
        "name", 
        "photo_thumb", # <-- ADDED THIS LINE
    )
    search_fields = ("name",)


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    """Admin interface for Collection model"""
    list_display = ("name_en", "name_es", "slug")
    search_fields = ("name_en", "name_es",)
    prepopulated_fields = {"slug": ("name_en",)}


@admin.register(Poem)
class PoemAdmin(SummernoteModelAdmin):
    """Admin interface for Poem model"""
    # --- 1. PREVIEW IMAGE ---
    @admin.display(description="Image")
    def thumb(self, obj):
        if (getattr(obj, "featured_image", None)
                and "placeholder" not in str(obj.featured_image)):

            img_html = (
                '<img src="{}" style="height:40px;border-radius:4px;">'
            )
            return format_html(img_html, obj.featured_image.url)
        return "—"

    # --- 2. CUSTOM COLUMN HEADERS ---
    @admin.display(description="Title (English)")
    def primary_title(self, obj):
        # Explicitly show the English title
        return obj.title_en

    @admin.display(description="Featured?", boolean=True)
    def is_featured_display(self, obj):
        return obj.is_featured

    @admin.display(description="Free PDF?", boolean=True)
    def is_free_lead_magnet_display(self, obj):
        return obj.is_free_lead_magnet

    # --- 3. UPDATED LIST DISPLAY ---
    # We now use our custom function names
    list_display = (
        "thumb",
        "primary_title",  # <-- Was "title_es"
        "author",
        "collection",
        "likes_count",
        "is_featured_display",  # <-- Was "is_featured"
        "is_free_lead_magnet_display",
        "created"
    )
    list_filter = ("collection", "is_featured", "is_free_lead_magnet", "created")
    ordering = ("-likes_count", "-created")
    search_fields = ("title_es", "title_en", "body_es", "body_en")

    # This will pre-fill the slug from the English title as you type
    prepopulated_fields = {"slug": ("title_en",)}

    # show the upload widget on the form
    fields = (
        "author", "collection",
        "featured_image",
        "title_en", "body_en",  # <-- English fields first
        "title_es", "body_es",  # <-- Spanish fields second
        "slug", "is_featured", "is_free_lead_magnet",
    )

    # rich editor for poem bodies
    summernote_fields = ("body_es", "body_en")

# --- 4. ERROR REMOVED ---
# The duplicate 'thumb' function that was here has been deleted.
