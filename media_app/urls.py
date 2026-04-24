from django.urls import path
from . import views

urlpatterns = [
    path('', views.media_home, name='media_home'),
]
