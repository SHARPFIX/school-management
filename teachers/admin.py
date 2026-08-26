from django.contrib import admin

from .models import teacher

@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display =(
        'employee_id',
        'first_name',
        'last_name',
        'school',
        'qaulification',
        'employement_type',
        'is_class_teacher',
        'email',
        'phone_number',
        'is_active',
    )
    list_filter =(
        'school',
        'employement_type',
        'gender',
        'is_class_teacher',
        'is_active',
    )
    search_fields =(
        'employee_id',
        'first_name',
        'last_name',
        'email',
        'phone',
        'school__school_name',

    )

    readonly_fields =(
        'created_at',
        'updated_at',
    )
    ordering =('school','first_name',)
    fieldsets = (
    (
        "School Information",
        {
            "fields": (
                "school",
                "user",
                "employee_id",
            )
        },
    ),

    (
        "Personal Information",
        {
            "fields": (
                "first_name",
                "last_name",
                "gender",
                "date_of_birth",
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
            )
        },
    ),

    (
        "Professional Information",
        {
            "fields": (
                "qaulification",
                "specialization",
                "experience",
                "employement_type",
                "joining_date",
                "salary",
            )
        },
    ),

    (
        "Status",
        {
            "fields": (
                "is_class_teacher",
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