from django.contrib import admin

from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "admission_number",
        "first_name",
        "last_name",
        "school",
        "gender",
        "roll_number",
        "is_active",
    )

    list_filter = (
        "school",
        "gender",
        "is_active",
    )

    search_fields = (
        "admission_number",
        "roll_number",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "father_name",
        "mother_name",
        "school__school_name",
    )

    readonly_fields = (
        "admission_number",
        "created_at",
        "updated_at",
    )

    ordering = (
        "school",
        "first_name",
        "last_name",
    )

    fieldsets = (

        (
            "School Information",
            {
                "fields": (
                    "school",
                    "user",
                )
            },
        ),

        (
            "Student Identification",
            {
                "fields": (
                    "admission_number",
                    "roll_number",
                )
            },
        ),

        (
            "Personal Information",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "date_of_birth",
                    "gender",
                    "photo",
                )
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "email",
                    "phone_number",
                    "address",
                    "city",
                    "state",
                )
            },
        ),

        (
            "Parent / Guardian",
            {
                "fields": (
                    "father_name",
                    "mother_name",
                    "parent_phone",
                )
            },
        ),

        (
            "Status",
            {
                "fields": (
                    "is_active",
                )
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )