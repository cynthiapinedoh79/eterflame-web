from django.urls import path
from . import views

urlpatterns = [
    path("", views.works_home, name="works_home"),
    path("design/", views.design, name="design"),
    path("media/", views.media, name="media"),
    path("studio/", views.studio, name="studio"),
]
