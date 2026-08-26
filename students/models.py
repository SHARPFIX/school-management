from django.db import models
from django.conf import settings

from schools.models import School


class Student(models.Model):

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    # ==========================
    # SCHOOL
    # ==========================

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="students"
    )

    # ==========================
    # LOGIN ACCOUNT
    # ==========================

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    # ==========================
    # STUDENT IDENTIFICATION
    # ==========================

    admission_number = models.CharField(
        max_length=30,
        unique=True,
        blank=True
    )

    roll_number = models.CharField(
        max_length=30,
        blank=True
    )

    # ==========================
    # PERSONAL INFORMATION
    # ==========================

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100,
        blank=True
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True
    )

    # ==========================
    # CONTACT
    # ==========================

    email = models.EmailField(
        blank=True
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    # ==========================
    # ADDRESS
    # ==========================

    address = models.TextField(
        blank=True
    )

    city = models.CharField(
        max_length=100,
        blank=True
    )

    state = models.CharField(
        max_length=100,
        blank=True
    )

    # ==========================
    # PARENT / GUARDIAN
    # ==========================

    father_name = models.CharField(
        max_length=150,
        blank=True
    )

    mother_name = models.CharField(
        max_length=150,
        blank=True
    )

    parent_phone = models.CharField(
        max_length=20,
        blank=True
    )

    # ==========================
    # PHOTO
    # ==========================

    photo = models.ImageField(
        upload_to="student_photos/",
        blank=True,
        null=True
    )

    # ==========================
    # STATUS
    # ==========================

    is_active = models.BooleanField(
        default=True
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
        ordering = [
            "first_name",
            "last_name"
        ]

    def save(self, *args, **kwargs):

        if not self.admission_number:

            last_student = Student.objects.filter(
                school=self.school
            ).order_by("-id").first()

            if last_student:
                number = last_student.id + 1
            else:
                number = 1

            self.admission_number = f"ADM-{number:05d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"