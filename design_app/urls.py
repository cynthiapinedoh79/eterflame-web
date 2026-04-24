from django.urls import path
from . import views

urlpatterns = [
    path('', views.design_home, name='design_home'),
]
