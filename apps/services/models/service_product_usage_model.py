"""
This file contains the definition of the service_product_usage model
"""

from django.db import models

from apps.core.models import TimeStampedModel
from apps.inventory.models import Product
from apps.services.models import Service


class ServiceProductUsage(TimeStampedModel):
    """
    This model is used to define the service_product_usage table.
    """

    quantity_used = models.FloatField()

    service = models.ForeignKey(
        Service,
        related_name="service_product_usage",
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        Product,
        related_name="service_product_usage",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.service.name + " - " + self.product.name
