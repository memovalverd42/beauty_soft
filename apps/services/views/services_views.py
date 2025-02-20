"""
This file contains the definition of the service view set
"""

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.services.models import Service
from apps.services.serializers import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """
    This class is used to define the service view set
    """

    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ["name", "price", "duration", "is_active"]
    ordering_fields = ["name", "price", "duration", "is_active"]
    filterset_fields = ["name", "price", "duration", "is_active"]

    def perform_create(self, serializer: ServiceSerializer) -> None:
        """
        This method overrides the perform_create method to associate the service with the current user.
        """
        serializer.save(user=self.request.user)

    def destroy(self, request: Request, *args, **kwargs):
        """
        This method is used to delete a service
        """
        instance: Service = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
