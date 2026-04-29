from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing and organised profile credential fields
    in the admin panel.
    """

    summernote_fields = ('content',)

    fieldsets = (
        ("Core Profile", {
            "fields": (
                "title",
                "subtitle",
                "profile_image",
                "content",
            )
        }),
        ("Core Expertise", {
            "fields": (
                "credential_title",
                "credential_subtitle",
                "credential_summary",
                "skills",
            )
        }),
        ("Technical Breakdown", {
            "fields": (
                ("skill_category_1_title", "skill_category_1_skills"),
                ("skill_category_2_title", "skill_category_2_skills"),
                ("skill_category_3_title", "skill_category_3_skills"),
            )
        }),
        ("Focus Areas", {
            "fields": (
                ("focus_1_title", "focus_1_text"),
                ("focus_2_title", "focus_2_text"),
                ("focus_3_title", "focus_3_text"),
            )
        }),
    )

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    panel for CollaborateRequest model.
    """

    list_display = ('message', 'read',)
