"""
This file is used to define the views for the product model.
"""

from rest_framework import viewsets, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.inventory.models import Product
from apps.inventory.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    This class defines the view set for the Product model.
    """

    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ["category", "price"]
    search_fields = ["name", "category__name"]
    ordering_fields = ["name", "price"]
    ordering = ["name", "price"]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 50
    pagination_class.page_size_query_param = "page_size"
    pagination_class.max_page_size = 100

    def perform_create(self, serializer: ProductSerializer) -> None:
        """
        This method overrides the perform_create method to associate the product with the current user.
        """
        serializer.save(user=self.request.user)

    def destroy(self, request: Request, *args, **kwargs):
        """
        Perform a destroy action on the Product instance.
        """
        instance: Product = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
