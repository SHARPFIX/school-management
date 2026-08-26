from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django .http import HttpResponse

from .forms import SchoolAdminRegistrationForm


def login_view(request):

    # If already logged in
    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect_user(user)

        messages.error(
            request,
            "Invalid username or password."
        )

    return render(
        request,
        "accounts/login.html"
    )


def redirect_user(user):

    # =========================
    # PLATFORM ADMIN
    # =========================

    if user.is_superuser or user.role == "super_admin":
        return redirect("admins:dashboard_admins")


    # =========================
    # SCHOOL ADMIN
    # =========================

    if user.role == "school_admin":
        return redirect("schools:dashboard")


    # =========================
    # TEACHER
    # =========================

    if user.role == "teacher":
        return redirect("teachers:dashboard")


    # =========================
    # STUDENT
    # =========================

    if user.role == "student":
        return redirect("students:dashboard")


    # =========================
    # PARENT
    # =========================

    if user.role == "parent":
        return redirect("parents:dashboard")


    # Fallback
    return redirect("/")


def register_view(request):

    # Don't allow logged-in users to register again
    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == "POST":

        form = SchoolAdminRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            # Automatically login after registration
            login(request, user)

            # Send them to Step 2
            return redirect("schools:register")

    else:

        form = SchoolAdminRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form
        }
    )


def logout_view(request):

    logout(request)

    return redirect("/")
def profile_view(request):
    return HttpResponse("Profile")

from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    return redirect("/")

from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SchoolAdminRegistrationForm


def signup_view(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":

        form = SchoolAdminRegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return redirect("/")

    else:

        form = SchoolAdminRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        }
    )