from django.urls import path
from . import views

urlpatterns = [
    path('', views.design_home, name='design_home'),
    path('case-study/conversion-predictor/', views.case_study_conversion, name='case_study_conversion'),
    path('case-study/<slug:slug>/', views.case_study_detail, name='case_study_detail'),
]
