from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from schools.models import School
from teachers.models import teacher

user = get_user_model()
@login_required
def dashboard(request):
    if   request.user.role != "super_admin" :
        return render(request, "admins/acess_denied.html")
    context ={
        "total_schools": School.objects.count(),
        #"active_schools": School.objects.filter(is_active=True).count(),
        "total_teachers": teacher.objects.count(),
        "total_users": user.objects.count(),
        #"pending_schools": teacher.objects.filter(is_approved=False).count(),
        
    }
    return render(request, "admins/dashboard_admins.html", context)

#def access_denied(request):
    return render(request, "admins/acess_denied.html")