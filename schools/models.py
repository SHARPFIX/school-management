from django.db import models
from django.conf import settings


class School(models.Model):

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("suspended", "Suspended"),
    ]

    PLAN_CHOICES = [
        ("free", "Free"),
        ("basic", "Basic"),
        ("premium", "Premium"),
        ("enterprise", "Enterprise"),
    ]

    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="school"
    )

    # ==========================
    # BASIC INFORMATION
    # ==========================

    school_name = models.CharField(
        max_length=200
    )

    school_code = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    # ==========================
    # CONTACT
    # ==========================

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=20
    )

    # ==========================
    # ADDRESS
    # ==========================

    address = models.TextField()

    city = models.CharField(
        max_length=100
    )

    state = models.CharField(
        max_length=100
    )

    country = models.CharField(
        max_length=100,
        default="India"
    )

    postal_code = models.CharField(
        max_length=10
    )

    # ==========================
    # SCHOOL DETAILS
    # ==========================

    principal_name = models.CharField(
        max_length=150
    )

    established_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    # ==========================
    # BRANDING
    # ==========================

    logo = models.ImageField(
        upload_to="school_logos/",
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True
    )

    # ==========================
    # SaaS
    # ==========================

    plan = models.CharField(
        max_length=20,
        choices=PLAN_CHOICES,
        default="free"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    is_verified = models.BooleanField(
        default=False
    )

    # ==========================
    # AUDIT
    # ==========================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["school_name"]

    def __str__(self):
        return self.school_name

    def save(self, *args, **kwargs):

        if not self.school_code:

            last_school = School.objects.order_by(
                "-id"
            ).first()

            if last_school:
                number = last_school.id + 1
            else:
                number = 1

            self.school_code = f"SCH-{number:05d}"

        super().save(*args, **kwargs)