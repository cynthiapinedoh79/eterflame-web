from django.urls import path
from . import views

app_name = 'works'

urlpatterns = [
    path('', views.works_home, name='works_home'),
    path('contact/', views.contact, name='contact'),
    path('contact/subscribe/', views.subscribe_lead, name='subscribe_lead'),
    path('works/', views.works_page, name='works_page'),
    path('works/resources/', views.resources, name='resources'),
]
