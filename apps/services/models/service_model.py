"""
This file contains the definition of the service model
"""

from django.conf import settings
from django.db import models

from apps.core.models import TimeStampedModel, IsActiveModel


class Service(TimeStampedModel, IsActiveModel):
    """
    This model is used to define the services table.
    """

    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.FloatField(null=True, blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="services",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "services"
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} - ${self.price}"
