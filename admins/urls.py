from django.urls import path
from . import views    
app_name = "admins"
urlpatterns = [
    path("dashboard_admins/", views.dashboard, name="dashboard_admins"),
    #path("acess_denied/", views.acess_denied, name="acess_denied")
]
