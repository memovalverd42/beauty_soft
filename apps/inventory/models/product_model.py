"""
This file contains the definition of the Product model.
"""

from django.conf import settings
from django.db import models
from apps.core.models import TimeStampedModel, IsActiveModel
from apps.inventory.models import Category


class Product(TimeStampedModel, IsActiveModel):
    """
    This class defines the Product model.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    low_stock_threshold = models.PositiveIntegerField(default=10)

    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="products",
        on_delete=models.CASCADE,
    )

    # Managers
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "products"
        ordering = ["-created"]

    def __str__(self) -> str:
        return f"{self.name} - ${self.price}"

    def is_low_stock(self) -> bool:
        """
        This method checks if the product is low in stock.
        """
        return self.quantity <= self.low_stock_threshold
