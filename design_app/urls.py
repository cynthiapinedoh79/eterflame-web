from django.urls import path
from . import views

urlpatterns = [
    path('', views.design_home, name='design_home'),
    path('case-study/conversion-predictor/', views.case_study_conversion, name='case_study_conversion'),
]
