"""
This file contains the admin classes for the product model
"""

from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from apps.inventory.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    This class defines the ProductAdmin class.
    """

    list_display = ("name", "price", "quantity", "category", "is_active")
    list_filter = ("category", "is_active")
    search_fields = ("name", "category__name")
    list_per_page = 10
    ordering = ("name", "price")
    fieldsets = (
        (None, {"fields": ("name", "description", "price", "quantity", "category")}),
        (
            "Opciones Avanzadas",
            {"classes": ("collapse",), "fields": ("low_stock_threshold",)},
        ),
    )
    actions = ["mark_as_low_stock"]

    def mark_as_low_stock(
        self, request: HttpRequest, queryset: QuerySet[Product]
    ) -> None:
        """
        This method marks the selected products as low stock.
        """
        queryset.update(quantity=0)
        self.message_user(
            request,
            "Los productos seleccionados han sido marcados como bajos de stock.",
        )

    mark_as_low_stock.short_description = "Marcar como bajo stock"
