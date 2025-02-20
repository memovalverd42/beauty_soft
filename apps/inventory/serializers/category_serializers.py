"""
This file contains the definition for the category model serializers.
"""

from rest_framework import serializers

from apps.inventory.models import Category


class CategorySerializer(serializers.ModelSerializer):
    """
    This class defines the CategorySerializer class.
    """

    class Meta:
        model = Category
        fields = ["id", "name", "description"]
        read_only_fields = ["id", "created", "modified"]
