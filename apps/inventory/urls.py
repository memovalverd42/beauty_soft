"""
This file contains the URL patterns for the inventory app.
"""

from django.urls import path, include
from rest_framework import routers

from apps.inventory.views import ProductViewSet, CategoryViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r"products", ProductViewSet, basename="product")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(router.urls)),
]
