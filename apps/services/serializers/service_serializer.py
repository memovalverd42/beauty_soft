"""
This file contains the serializers for the services' entity.
"""

from rest_framework import serializers

from apps.services.models import Service


class ServiceSerializer(serializers.ModelSerializer):
    """
    This class is used to serialize the services' entity.
    """

    class Meta:
        model = Service
        fields = [
            "id",
            "name",
            "description",
            "price",
            "duration",
            "is_active",
            "created",
        ]
        read_only_fields = ["id", "created", "modified"]
