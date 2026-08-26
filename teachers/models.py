
from django.db import models
from django.conf import settings
from schools.models import School
class teacher(models.Model):
    GENDER_CHOICES =[('M', 'Male'), ('F', 'Female'), ('O', 'Other')
                     ]

    EMPLOYENENT_CHOICES =[('FT', 'Full Time'), ('PT', 'Part Time'),('CT', 'Contract')]

    school =models.ForeignKey(School,on_delete=models.CASCADE,related_name='teachers')
    user =models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher_profile')

    employee_id =models.CharField(max_length=20, unique=True)

    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email =models.EmailField(unique=True)
    phone_number =models.CharField(max_length=20, blank=True)
    gender =models.CharField(max_length=1, choices=GENDER_CHOICES)

    date_of_birth =models.DateField()

    qaulification =models.CharField(max_length=100)

    specialization =models.CharField(max_length=100)    

    experience =models.PositiveIntegerField(
        help_text="Enter the number of years of experience"
    )

    employement_type =models.CharField(max_length=2, choices=EMPLOYENENT_CHOICES)

    joining_date =models.DateField()

    salary =models.DecimalField(max_digits=10, decimal_places=2)

    photo =models.ImageField(upload_to='teacher_photos/', blank=True, null=True)

    is_class_teacher =models.BooleanField(default=False)

    is_active=models.BooleanField(default=True)

    created_at =models.DateTimeField(auto_now_add=True)

    updated_at =models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['first_name', ]

    def __str__(self):
        return f"{self.first_name}"
# Create your models here.

class TeacherAttendance(models.Model):

    STATUS_CHOICES = [
        ("present", "Present"),
        ("absent", "Absent"),
        ("leave", "Leave"),
        ("half_day", "Half Day"),
    ]

    teacher = models.ForeignKey(
        teacher,
        on_delete=models.CASCADE,
        related_name="attendance_records"
    )

    date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="present"
    )

    remarks = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        ordering = [
            "-date",
            "teacher__first_name",
        ]

        constraints = [
            models.UniqueConstraint(
                fields=["teacher", "date"],
                name="unique_teacher_attendance_per_day"
            )
        ]

    def __str__(self):

        return (
            f"{self.teacher.first_name} "
            f"{self.teacher.last_name} - "
            f"{self.date} - "
            f"{self.status}"
        )
