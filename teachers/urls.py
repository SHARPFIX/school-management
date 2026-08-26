from django.urls import path
from . import views

app_name = "teachers"

urlpatterns = [

    # Teacher's own dashboard
    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    # School Admin teacher management
    path(
        "manage/",
        views.teacher_management,
        name="management"
    ),

    path(
        "manage/list/",
        views.teacher_list,
        name="list"
    ),

    path(
        "manage/add/",
        views.teacher_add,
        name="add"
    ),

    path(
        "manage/<int:pk>/",
        views.teacher_detail,
        name="detail"
    ),
    path(
    "manage/attendance/",
    views.teacher_attendance,
    name="attendance"
),

path(
    "manage/attendance/save/",
    views.save_teacher_attendance,
    name="save_attendance"
),
]