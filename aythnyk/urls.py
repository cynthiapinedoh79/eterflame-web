from django.urls import path
from . import views
app_name = "aythnyk"
urlpatterns = [
    path("", views.aythnyk_home, name="aythnyk_home"),
    path("tools/", views.aythnyk_tools, name="aythnyk_tools"),
]
