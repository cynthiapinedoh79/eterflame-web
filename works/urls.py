from django.urls import path
from . import views

app_name = 'works'

urlpatterns = [
    path('', views.works_home, name='works_home'),
    path('works/design/', views.design, name='design'),
    path('works/media/', views.media, name='media'),
    path('works/studio/', views.studio, name='studio'),
]
