"""
This file is used to define the views for the users app.
"""

from django.contrib.auth import login
from django.http import HttpRequest
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnoxLogoutAllView,
)
from rest_framework import permissions, generics
from rest_framework.response import Response

from apps.core.serializers import EmptySerializer
from apps.users.serializers import AuthSerializer, UserSerializer


class LoginView(KnoxLoginView):
    """
    This class defines the LoginView. It extends KnoxLoginView.
    """

    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request: HttpRequest, format=None) -> Response:
        """
        This method is used to handle the POST request for the LoginView.
        :param request: Request object
        :param format: str
        :return: Response object
        """
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class LogoutView(KnoxLogoutView, generics.GenericAPIView):
    """
    This class defines the CustomLogoutView. It extends KnoxLogoutView.
    """

    serializer_class = EmptySerializer
    permission_classes = (permissions.IsAuthenticated,)


class LogoutAllView(KnoxLogoutAllView, generics.GenericAPIView):
    """
    This class defines the CustomLogoutAllView. It extends KnoxLogoutAllView.
    """

    serializer_class = EmptySerializer
    permission_classes = (permissions.IsAuthenticated,)


class ManageUserView(generics.RetrieveAPIView):
    """
    Manage the authenticated user
    """

    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
