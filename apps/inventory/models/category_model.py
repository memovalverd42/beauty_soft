"""
This file contains the definition of the Category model.
"""

from django.conf import settings
from django.db import models
from apps.core.models import TimeStampedModel


class Category(TimeStampedModel):
    """
    This class defines the Category model.
    """

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="categories",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "categories"
        ordering = ["-created"]

    # Managers
    objects = models.Manager()

    def __str__(self):
        return self.name
