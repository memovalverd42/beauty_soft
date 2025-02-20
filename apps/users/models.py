"""
This file contains the custom User model
"""

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    """
    This class defines the CustomUserManager.
    """

    def _create_user(
        self, email, password, first_name, last_name, is_email_verified, **extra_fields
    ):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password must be provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            is_email_verified=is_email_verified,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        is_email_verified: bool,
        **extra_fields,
    ) -> "User":
        """
        This method creates a user.
        """
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(
            email, password, first_name, last_name, is_email_verified, **extra_fields
        )

    def create_superuser(
        self,
        email: str,
        password: str,
        first_name: str,
        last_name: str,
        is_email_verified: bool,
        **extra_fields,
    ) -> "User":
        """
        This method creates a superuser.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(
            email, password, first_name, last_name, is_email_verified, **extra_fields
        )


class User(AbstractBaseUser, PermissionsMixin):
    """
    This class defines the User model.
    """

    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "is_email_verified"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
