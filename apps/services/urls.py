"""
This file contains the urls for the services' app.
"""

from django.urls import path, include
from rest_framework import routers

from apps.services.views import ServiceViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"services", ServiceViewSet, basename="service")

urlpatterns = [
    path("", include(router.urls)),
]
