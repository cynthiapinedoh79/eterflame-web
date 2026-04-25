from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('prints/', views.prints, name='prints'),
    path('digital/', views.digital, name='digital'),
    path('commission/', views.commission, name='commission'),
]
