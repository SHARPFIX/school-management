from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import School
from .forms import SchoolRegistrationForm


# ==========================================
# SCHOOL LIST
# ==========================================

@login_required
def school_list(request):

    # Only platform admins can see all schools
    if not request.user.is_superuser and request.user.role != "super_admin":
        return redirect("/")

    schools = School.objects.all()

    return render(
        request,
        "schools/list.html",
        {
            "schools": schools
        }
    )


# ==========================================
# SCHOOL REGISTRATION
# ==========================================

@login_required
def school_register(request):

    # Only school administrators
    if request.user.role not in[ "school_admin","super_admin"]:
        return redirect("/")

    # Prevent the same administrator
    # from registering multiple schools
    if hasattr(request.user, "school"):
        return redirect("schools:dashboard")

    if request.method == "POST":

        form = SchoolRegistrationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            school = form.save(commit=False)

            # Connect school to logged-in administrator
            school.owner = request.user

            school.save()

            return redirect("schools:dashboard")

    else:

        form = SchoolRegistrationForm()

    return render(
        request,
        "schools/register.html",
        {
            "form": form
        }
    )


# ==========================================
# SCHOOL DETAIL
# ==========================================

@login_required
def school_detail(request, pk):

    school = School.objects.get(pk=pk)

    return render(
        request,
        "schools/detail.html",
        {
            "school": school
        }
    )


# ==========================================
# SCHOOL UPDATE
# ==========================================

@login_required
def school_update(request, pk):

    school = School.objects.get(pk=pk)

    return HttpResponse(
        f"Update School: {school.school_name}"
    )


# ==========================================
# SCHOOL DELETE
# ==========================================

@login_required
def school_delete(request, pk):

    school = School.objects.get(pk=pk)

    return HttpResponse(
        f"Delete School: {school.school_name}"
    )


# ==========================================
# SCHOOL ADMIN DASHBOARD
# ==========================================

@login_required
def dashboard(request):

    # Only school administrators
    if request.user.role != "school_admin":
        return redirect("/")

    # Get school belonging to logged-in admin
    try:

        school = request.user.school

    except School.DoesNotExist:

        return render(
            request,
            "schools/no_school.html"
        )

    # Count teachers belonging to this school
    total_teachers = school.teachers.count()

    context = {
        "school": school,

        "total_teachers": total_teachers,

        # We will connect these later
        "total_students": 0,

        "total_classes": 0,

        "attendance_percentage": 0,
    }

    return render(
        request,
        "schools/dashboard.html",
        context
    )

