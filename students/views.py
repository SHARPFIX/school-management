from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from .forms import StudentForm
from .models import Student
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def dashboard(request):

    # Only students can access this dashboard
    if request.user.role != "student":
        return redirect("/")

    try:

        student = request.user.student_profile

    except Student.DoesNotExist:

        return render(
            request,
            "students/no_profile.html"
        )

    context = {
        "student": student,

        # We will connect these to real models later
        "attendance_percentage": 0,
        "total_subjects": 0,
        "pending_assignments": 0,
        "upcoming_exams": 0,
    }

    return render(
        request,
        "students/dashboard.html",
        context
    )
@login_required
def students_list(request):
    #only school admin will be access
    if request.user.role !="school_admin":
        return redirect("/")
    try:
        school = request.user.school
    except AttributeError:
        return redirect("/")
    students=Student.objects.filter(
        school=school
    ).order_by("first_name","last_name")


    #search
    search = request.GET.get("search","").strip()

    if search:
         
         students = students.filter(
        first_name__icontains=search
    ) | students.filter(
        last_name__icontains=search
    ) | students.filter(
        admission_number__icontains=search
    ) | students.filter(
        roll_number__icontains=search
    )
    #status bar
    status=request.GET.get("status")
    if status=="active":
        students = students.filter(is_active=True)
    elif status=="inactive":
        students = students.filter(is_active=False)

    context={

        "students":students,
        "search":search,
        "status":status,
        "school":school,
    }
    return render(request,"students/student_list.html",context)


@login_required
def student_detail(request,pk):
    if request.user.role != "school_admin":
        return redirect("/")
    try:
        school = request.user.school
    except AttributeError:
        return redirect("/")
    student = get_object_or_404(
        Student,
        pk=pk,
        school=school
        )
    return render(request,"students/students_detail.html",{
        "student":student,
        "school":school,

    })
    
# add student view 
from django.db import transaction
from uuid import uuid4

@login_required
def student_add(request):

    # Only school admin can add students
    if request.user.role != "school_admin":
        return redirect("/")

    # Get the school of the logged-in admin
    try:
        school = request.user.school
    except AttributeError:
        return redirect("/")

    if request.method == "POST":

        form = StudentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            with transaction.atomic():

                # Get student information from form
                first_name = form.cleaned_data["first_name"]
                last_name = form.cleaned_data["last_name"]
                email = form.cleaned_data["email"]

                # Temporary unique username
                temporary_username = (
                    "student_" + uuid4().hex[:10]
                )

                # Create student login account FIRST
                user = User.objects.create_user(
                    username=temporary_username,
                    password="Student@123",
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    role="student",
                )

                # Create student
                student = form.save(commit=False)

                # Automatically assign school
                student.school = school

                # Connect student with user
                student.user = user

                # Save student
                student.save()

                # Now admission_number has been generated
                # by Student.save()

                # Change username to admission number
                user.username = student.admission_number
                user.save(
                    update_fields=["username"]
                )

            return redirect(
                "students:detail",
                pk=student.pk
            )

    else:
        form = StudentForm()

    return render(
        request,
        "students/add_student.html",
        {
            "form": form,
            "school": school,
        }
    )