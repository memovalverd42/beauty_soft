"""
This file is used to define the URL patterns for the users app.
"""

from django.urls import path

from apps.users.views import LoginView, LogoutView, LogoutAllView, ManageUserView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("logoutall/", LogoutAllView.as_view(), name="logout-all"),
    path("profile/", ManageUserView.as_view(), name="profile"),
]
