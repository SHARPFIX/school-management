from django.urls import path

from . import views


app_name = "students"


urlpatterns = [

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),
    path("student_list/",views.students_list,name="list"),

     path(
        "<int:pk>/",
        views.student_detail,
        name="detail"
    ),

    path("add_student/", views.student_add, name="add"),



]