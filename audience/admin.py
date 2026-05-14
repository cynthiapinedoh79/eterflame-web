from django.contrib import admin
from .models import Subscriber


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "name",
        "source",
        "is_active_display",
        "created_at",
    )
    list_filter = ("source", "confirmed", "created_at")
    search_fields = ("email", "name")
    readonly_fields = ("created_at",)
    date_hierarchy = "created_at"
    ordering = ("-created_at",)

    fieldsets = (
        (None, {
            "fields": ("email", "name", "source", "confirmed"),
        }),
        ("Status", {
            "fields": ("unsubscribed_at", "created_at"),
        }),
    )

    actions = ["mark_as_unsubscribed", "export_emails_csv"]

    @admin.display(boolean=True, description="Active")
    def is_active_display(self, obj):
        return obj.is_active

    @admin.action(description="Mark selected as unsubscribed")
    def mark_as_unsubscribed(self, request, queryset):
        from django.utils import timezone
        count = queryset.filter(unsubscribed_at__isnull=True).update(
            unsubscribed_at=timezone.now()
        )
        self.message_user(request, f"{count} subscriber(s) unsubscribed.")

    @admin.action(description="Export emails as CSV")
    def export_emails_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="subscribers.csv"'
        writer = csv.writer(response)
        writer.writerow(["email", "name", "source", "created_at", "active"])
        for sub in queryset:
            writer.writerow([
                sub.email,
                sub.name,
                sub.source,
                sub.created_at.isoformat(),
                sub.is_active,
            ])
        return response