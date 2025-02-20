"""
This file contains the auth serializers.
"""

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer

from apps.users.models import User


class UserSerializer(ModelSerializer):
    """
    This class defines the UserSerializer.
    """

    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 5},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)


class AuthSerializer(Serializer):
    """
    This class defines the AuthSerializer.
    """

    email = serializers.EmailField()
    password = serializers.CharField(
        trim_whitespace=False,
    )

    def validate(self, attrs: dict) -> dict:
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise serializers.ValidationError("Invalid password")
        else:
            raise serializers.ValidationError("Email and password are required")

        attrs["user"] = user
        return attrs
