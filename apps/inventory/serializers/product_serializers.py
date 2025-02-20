"""
This file contains the definition for the product model serializers.
"""

from rest_framework import serializers

from apps.inventory.models import Product
from apps.inventory.serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    """
    This class defines the ProductSerializer class.
    """

    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "quantity",
            "low_stock_threshold",
            "category",
        ]
        read_only_fields = ["id", "created", "modified"]
