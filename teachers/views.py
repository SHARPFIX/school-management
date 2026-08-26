from uuid import uuid4
from datetime import date

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count, Q
from django.shortcuts import render, redirect, get_object_or_404

from .models import teacher, TeacherAttendance
from .forms import TeacherForm


User = get_user_model()


# =========================================================
# TEACHER - OWN DASHBOARD
# =========================================================

@login_required
def dashboard(request):

    # Only teachers can access this dashboard
    if request.user.role != "teacher":
        return redirect("/")

    try:
        teacher_profile = request.user.teacher_profile

    except teacher.DoesNotExist:
        return render(
            request,
            "teachers/no_profile.html"
        )

    # =====================================================
    # TEACHER ATTENDANCE
    # =====================================================

    attendance_records = TeacherAttendance.objects.filter(
        teacher=teacher_profile
    )

    total_attendance = attendance_records.count()

    present_count = attendance_records.filter(
        status="present"
    ).count()

    absent_count = attendance_records.filter(
        status="absent"
    ).count()

    leave_count = attendance_records.filter(
        status="leave"
    ).count()

    half_day_count = attendance_records.filter(
        status="half_day"
    ).count()

    # Attendance percentage
    if total_attendance > 0:

        attendance_percentage = round(
            (
                present_count
                / total_attendance
            ) * 100,
            1
        )

    else:

        attendance_percentage = 0

    context = {

        "teacher": teacher_profile,

        # Existing dashboard values
        "total_students": 0,
        "total_classes": 0,
        "today_classes": 0,

        # Attendance
        "attendance_percentage":
            attendance_percentage,

        "total_attendance":
            total_attendance,

        "present_count":
            present_count,

        "absent_count":
            absent_count,

        "leave_count":
            leave_count,

        "half_day_count":
            half_day_count,
    }

    return render(
        request,
        "teachers/dashboard.html",
        context
    )
# =========================================================
# SCHOOL ADMIN - TEACHER MANAGEMENT DASHBOARD
# =========================================================

@login_required
def teacher_management(request):

    # Only School Admin
    if request.user.role != "school_admin":
        return redirect("/")

    # Get logged-in admin's school
    try:
        school = request.user.school

    except AttributeError:
        return redirect("/")


    # =====================================================
    # TEACHERS
    # =====================================================

    teachers = teacher.objects.filter(
        school=school
    ).order_by(
        "first_name",
        "last_name"
    )


    # =====================================================
    # TEACHER COUNTS
    # =====================================================

    total_teachers = teachers.count()

    active_teachers = teachers.filter(
        is_active=True
    ).count()

    inactive_teachers = teachers.filter(
        is_active=False
    ).count()

    class_teachers = teachers.filter(
        is_class_teacher=True
    ).count()


    # =====================================================
    # AVERAGE SALARY
    # =====================================================

    average_salary = teachers.aggregate(
        avg=Avg("salary")
    )["avg"] or 0


    # =====================================================
    # TEACHER ATTENDANCE
    # =====================================================

    attendance_stats = TeacherAttendance.objects.filter(
        teacher__school=school
    ).aggregate(

        total=Count("id"),

        present=Count(
            "id",
            filter=Q(status="present")
        )
    )


    total_attendance = (
        attendance_stats["total"] or 0
    )

    present_attendance = (
        attendance_stats["present"] or 0
    )


    # Calculate percentage

    if total_attendance > 0:

        teacher_attendance_percentage = round(
            (
                present_attendance
                / total_attendance
            ) * 100,
            1
        )

    else:

        teacher_attendance_percentage = 0


    # =====================================================
    # TODAY'S ATTENDANCE
    # =====================================================

    today = date.today()

    today_attendance = TeacherAttendance.objects.filter(
        teacher__school=school,
        date=today
    )


    today_present = today_attendance.filter(
        status="present"
    ).count()


    today_absent = today_attendance.filter(
        status="absent"
    ).count()


    today_leave = today_attendance.filter(
        status="leave"
    ).count()


    today_half_day = today_attendance.filter(
        status="half_day"
    ).count()


    # =====================================================
    # TODAY ATTENDANCE PERCENTAGE
    # =====================================================

    total_today = today_attendance.count()

    if total_today > 0:

        today_attendance_percentage = round(
            (
                today_present
                / total_today
            ) * 100,
            1
        )

    else:

        today_attendance_percentage = 0


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "school": school,

        "teachers": teachers,


        # Teacher statistics

        "total_teachers":
            total_teachers,

        "active_teachers":
            active_teachers,

        "inactive_teachers":
            inactive_teachers,

        "class_teachers":
            class_teachers,


        # Salary

        "average_salary":
            average_salary,


        # Overall attendance

        "teacher_attendance_percentage":
            teacher_attendance_percentage,

        "total_attendance":
            total_attendance,

        "present_attendance":
            present_attendance,


        # Today's attendance

        "today_present":
            today_present,

        "today_absent":
            today_absent,

        "today_leave":
            today_leave,

        "today_half_day":
            today_half_day,

        "today_attendance_percentage":
            today_attendance_percentage,
    }


    return render(
        request,
        "teachers/manage.html",
        context
    )


# =========================================================
# SCHOOL ADMIN - TEACHER LIST
# =========================================================

@login_required
def teacher_list(request):

    # Only School Admin
    if request.user.role != "school_admin":
        return redirect("/")

    # Get school
    try:
        school = request.user.school

    except AttributeError:
        return redirect("/")


    # Get teachers
    teachers = teacher.objects.filter(
        school=school
    ).order_by(
        "first_name",
        "last_name"
    )


    # =====================================================
    # SEARCH
    # =====================================================

    search = request.GET.get(
        "search",
        ""
    ).strip()


    if search:

        teachers = teachers.filter(

            Q(
                first_name__icontains=search
            )

            |

            Q(
                last_name__icontains=search
            )

            |

            Q(
                employee_id__icontains=search
            )

            |

            Q(
                email__icontains=search
            )
        )


    # =====================================================
    # STATUS FILTER
    # =====================================================

    status = request.GET.get(
        "status"
    )


    if status == "active":

        teachers = teachers.filter(
            is_active=True
        )


    elif status == "inactive":

        teachers = teachers.filter(
            is_active=False
        )


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "school": school,

        "teachers": teachers,

        "search": search,

        "status": status,
    }


    return render(
        request,
        "teachers/teacher_list.html",
        context
    )


# =========================================================
# SCHOOL ADMIN - TEACHER DETAIL
# =========================================================

@login_required
def teacher_detail(request, pk):

    # Only School Admin
    if request.user.role != "school_admin":
        return redirect("/")


    # Get school
    try:
        school = request.user.school

    except AttributeError:
        return redirect("/")


    # Security:
    # Admin can only access teachers from their school

    teacher_obj = get_object_or_404(
        teacher,
        pk=pk,
        school=school
    )


    # =====================================================
    # TEACHER ATTENDANCE STATISTICS
    # =====================================================

    attendance_records = TeacherAttendance.objects.filter(
        teacher=teacher_obj
    )


    total_attendance = attendance_records.count()


    present_count = attendance_records.filter(
        status="present"
    ).count()


    absent_count = attendance_records.filter(
        status="absent"
    ).count()


    leave_count = attendance_records.filter(
        status="leave"
    ).count()


    half_day_count = attendance_records.filter(
        status="half_day"
    ).count()


    if total_attendance > 0:

        attendance_percentage = round(
            (
                present_count
                / total_attendance
            ) * 100,
            1
        )

    else:

        attendance_percentage = 0


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "teacher": teacher_obj,

        "school": school,


        # Attendance

        "total_attendance":
            total_attendance,

        "present_count":
            present_count,

        "absent_count":
            absent_count,

        "leave_count":
            leave_count,

        "half_day_count":
            half_day_count,

        "attendance_percentage":
            attendance_percentage,
    }


    return render(
        request,
        "teachers/detail.html",
        context
    )


# =========================================================
# SCHOOL ADMIN - ADD TEACHER
# =========================================================

@login_required
def teacher_add(request):

    # Only School Admin
    if request.user.role != "school_admin":
        return redirect("/")


    # Get school
    try:
        school = request.user.school

    except AttributeError:
        return redirect("/")


    # =====================================================
    # POST
    # =====================================================

    if request.method == "POST":

        form = TeacherForm(
            request.POST,
            request.FILES
        )


        if form.is_valid():

            with transaction.atomic():

                # -----------------------------------------
                # Teacher information
                # -----------------------------------------

                first_name = form.cleaned_data[
                    "first_name"
                ]

                last_name = form.cleaned_data[
                    "last_name"
                ]

                email = form.cleaned_data[
                    "email"
                ]


                # -----------------------------------------
                # Temporary username
                # -----------------------------------------

                temporary_username = (
                    "teacher_"
                    + uuid4().hex[:10]
                )


                # -----------------------------------------
                # Create login account
                # -----------------------------------------

                user = User.objects.create_user(

                    username=temporary_username,

                    password="Teacher@123",

                    first_name=first_name,

                    last_name=last_name,

                    email=email,

                    role="teacher",
                )


                # -----------------------------------------
                # Create teacher
                # -----------------------------------------

                teacher_obj = form.save(
                    commit=False
                )


                # Automatically assign school

                teacher_obj.school = school


                # Connect teacher to user

                teacher_obj.user = user


                # Save teacher

                teacher_obj.save()


                # -----------------------------------------
                # Use employee ID as username
                # -----------------------------------------

                user.username = (
                    teacher_obj.employee_id
                )


                user.save(
                    update_fields=[
                        "username"
                    ]
                )


            return redirect(
                "teachers:detail",
                pk=teacher_obj.pk
            )


    # =====================================================
    # GET
    # =====================================================

    else:

        form = TeacherForm()


    return render(
        request,
        "teachers/add_teacher.html",
        {
            "form": form,
            "school": school,
        }
    )


# =========================================================
# SCHOOL ADMIN - TEACHER ATTENDANCE
# =========================================================

@login_required
def teacher_attendance(request):

    # Only School Admin
    if request.user.role != "school_admin":
        return redirect("/")


    # Get school
    try:
        school = request.user.school

    except AttributeError:
        return redirect("/")


    # =====================================================
    # SELECTED DATE
    # =====================================================

    selected_date = request.GET.get(
        "date"
    )


    if not selected_date:

        selected_date = date.today().isoformat()


    # =====================================================
    # ACTIVE TEACHERS
    # =====================================================

    teachers = teacher.objects.filter(
        school=school,
        is_active=True
    ).order_by(
        "first_name",
        "last_name"
    )


    # =====================================================
    # ATTENDANCE RECORDS
    # =====================================================

    attendance_records = TeacherAttendance.objects.filter(
        teacher__school=school,
        date=selected_date
    )


    # Create lookup map

    attendance_map = {

        record.teacher_id: record

        for record in attendance_records
    }


    # =====================================================
    # ATTENDANCE ROWS
    # =====================================================

    attendance_rows = []


    for teacher_obj in teachers:

        attendance_rows.append({

            "teacher":
                teacher_obj,

            "attendance":
                attendance_map.get(
                    teacher_obj.id
                ),
        })


    # =====================================================
    # COUNTS
    # =====================================================

    present_count = attendance_records.filter(
        status="present"
    ).count()


    absent_count = attendance_records.filter(
        status="absent"
    ).count()


    leave_count = attendance_records.filter(
        status="leave"
    ).count()


    half_day_count = attendance_records.filter(
        status="half_day"
    ).count()


    # =====================================================
    # ATTENDANCE PERCENTAGE FOR SELECTED DATE
    # =====================================================

    total_teachers = teachers.count()


    if total_teachers > 0:

        attendance_percentage = round(
            (
                present_count
                / total_teachers
            ) * 100,
            1
        )

    else:

        attendance_percentage = 0


    # =====================================================
    # CONTEXT
    # =====================================================

    context = {

        "school": school,

        "attendance_rows":
            attendance_rows,

        "selected_date":
            selected_date,


        "present_count":
            present_count,

        "absent_count":
            absent_count,

        "leave_count":
            leave_count,

        "half_day_count":
            half_day_count,


        "attendance_percentage":
            attendance_percentage,
    }


    return render(
        request,
        "teachers/attendance.html",
        context
    )


# =========================================================
# SCHOOL ADMIN - SAVE TEACHER ATTENDANCE
# =========================================================

@login_required
def save_teacher_attendance(request):

    # Only School Admin
    if request.user.role != "school_admin":
        return redirect("/")


    # Get school
    try:
        school = request.user.school

    except AttributeError:
        return redirect("/")


    # Only POST
    if request.method != "POST":

        return redirect(
            "teachers:attendance"
        )


    # =====================================================
    # GET POST DATA
    # =====================================================

    teacher_id = request.POST.get(
        "teacher_id"
    )

    attendance_date = request.POST.get(
        "date"
    )

    status = request.POST.get(
        "status"
    )

    remarks = request.POST.get(
        "remarks",
        ""
    ).strip()


    # =====================================================
    # VALIDATION
    # =====================================================

    if (
        not teacher_id
        or not attendance_date
        or not status
    ):

        return redirect(
            f"/teachers/manage/attendance/"
            f"?date={attendance_date}"
        )


    # =====================================================
    # VALID STATUS
    # =====================================================

    valid_statuses = {
        "present",
        "absent",
        "leave",
        "half_day",
    }


    if status not in valid_statuses:

        return redirect(
            f"/teachers/manage/attendance/"
            f"?date={attendance_date}"
        )


    # =====================================================
    # GET TEACHER
    # =====================================================

    teacher_obj = get_object_or_404(

        teacher,

        pk=teacher_id,

        school=school
    )


    # =====================================================
    # CREATE OR UPDATE
    # =====================================================

    TeacherAttendance.objects.update_or_create(

        teacher=teacher_obj,

        date=attendance_date,

        defaults={

            "status":
                status,

            "remarks":
                remarks,
        }
    )


    # =====================================================
    # RETURN TO ATTENDANCE PAGE
    # =====================================================

    return redirect(
        f"/teachers/manage/attendance/"
        f"?date={attendance_date}"
    )