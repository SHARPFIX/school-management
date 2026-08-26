from django.urls import path
from . import views

app_name = "schools"

urlpatterns = [
    path("", views.school_list, name="list"),
    path("register/", views.school_register, name="register"),
    path("<int:pk>/", views.school_detail, name="detail"),
    path("<int:pk>/edit/", views.school_update, name="update"),
    path("<int:pk>/delete/", views.school_delete, name="delete"),
    path("dashboard/",views.dashboard, name= "dashboard"),
    path("list/",views.school_list, name= "list"),
   
]