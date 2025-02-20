"""
This file contains the model for the IsActive model.
"""

from django.db import models


class IsActiveModel(models.Model):
    """
    This class defines the IsActive model.
    """

    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
