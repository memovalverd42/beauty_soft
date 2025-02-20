"""
This file contains the admin classes for the category model
"""

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from apps.inventory.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    This class defines the CategoryAdmin class.
    """

    list_display = ("name", "description")
    search_fields = ("name",)
    list_per_page = 10
    ordering = ("name",)
    fieldsets = ((None, {"fields": ("name", "description")}),)
    actions = ["delete_selected"]

    def delete_selected(
        self, request: HttpRequest, queryset: QuerySet[Category]
    ) -> None:
        """
        This method deletes the selected categories.
        """
        queryset.delete()
        self.message_user(request, "Las categorías seleccionadas han sido eliminadas.")

    delete_selected.short_description = "Eliminar seleccionados"
