from django.urls import path
from . import views
from design_app import views as design_views
from media_app import views as media_views
from studio_app import views as studio_views

app_name = 'works'

urlpatterns = [
    path('', views.works_home, name='works_home'),
    path('contact/', views.contact, name='contact'),
    path('works/resources/', views.resources, name='resources'),
    path('works/design/', design_views.design_home, name='design'),
    path('works/media/', media_views.media_home, name='media'),
    path('works/studio/', studio_views.studio_home, name='studio'),
]
