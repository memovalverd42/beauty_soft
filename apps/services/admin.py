"""
This file is used to define the admin interface for the services' app.
"""

from django.contrib import admin
from django.http import HttpRequest

from apps.services.models import Service, ServiceProductUsage


class ServiceProductUsageInline(admin.TabularInline):
    """
    This class is used to define the inline admin interface for ServiceProductUsage.
    """

    model = ServiceProductUsage
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    This class is used to define the service admin interface.
    """

    list_display = ("name", "price", "duration", "is_active")
    search_fields = ("name", "price", "duration", "is_active")
    list_filter = ("name", "price", "duration", "is_active")
    ordering = ("name", "price", "duration", "is_active")
    fieldsets = (
        (None, {"fields": ("name", "price", "duration", "is_active")}),
        ("Description", {"fields": ("description",), "classes": ("collapse",)}),
    )
    inlines = [ServiceProductUsageInline]

    def save_model(self, request: HttpRequest, obj: Service, form, change: bool):
        """
        This method overrides the save_model method to associate the service with the current user.
        """
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)
