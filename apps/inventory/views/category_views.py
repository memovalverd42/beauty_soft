"""
This file contains the views for the category model
"""

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.inventory.models import Category
from apps.inventory.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    This class defines the views for the Category model.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer: CategorySerializer):
        """
        This method overrides the perform_create method to associate the category with the current user.
        """
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        """
        Disable the DELETE method.
        """
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
