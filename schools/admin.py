from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import School


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = (
        "school_name",
        "school_code",
        "owner",
        "city",
        "state",
        "plan",
        "status",
        "is_verified",
        "created_at",
    )

    list_filter = (
        "plan",
        "status",
        "is_verified",
        "state",
        "city",
    )

    search_fields = (
        "school_name",
        "school_code",
        "email",
        "administrator__username",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    ordering = ("school_name",)

    fieldsets = (
        (
            "School Information",
            {
                "fields": (
                    "owner",
                    "school_name",
                    "school_code",
                    "logo",
                )
            },
        ),
        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone",
                    "website",
                )
            },
        ),
        (
            "Address",
            {
                "fields": (
                    "address",
                    "city",
                    "state",
                    "country",
                    "postal_code",
                )
            },
        ),
        (
            "School Details",
            {
                "fields": (
                    "principal_name",
                    "established_year",
                )
            },
        ),
        (
            "Subscription",
            {
                "fields": (
                    "plan",
                    "status",
                    "is_verified",
                )
            },
        ),
        (
            "Dates",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )