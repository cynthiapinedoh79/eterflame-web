from django.urls import path
from . import views


app_name = "audience"


urlpatterns = [
    path("", views.subscribe_view, name="subscribe"),
]
