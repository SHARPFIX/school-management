from django.db import models

# Create your models here.
# accounts/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = [
        ("super_admin", "Super Admin"),
        ("school_admin", "School Administrator"),
        ("teacher", "Teacher"),
        ("student", "Student"),
        ("parent", "Parent"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="school_admin",
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    profile_picture = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True
    )

    email_verified = models.BooleanField(default=False)

    is_active_school = models.BooleanField(default=True)

    def __str__(self):
        return self.username