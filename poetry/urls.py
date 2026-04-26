from django.urls import path
from . import views

app_name = "poetry"

urlpatterns = [
    # Home URL kept as an alias so existing references resolve to /aythnyk/.
    # The aythnyk app (mounted first) handles the actual request.
    path("", views.poetry_home, name="poetry_home"),
    path("poems/", views.poem_list, name="poem_list"),     # list moved here
    # IMPORTANT: prefix detail so it doesn't match /about/ or /blog/
    path("poem/<slug:slug>/", views.poem_detail, name="poem_detail"),
    path('author/<slug:slug>/', views.author_detail, name='author_detail'),

    # --- NEW URLS FOR FAVORITES ---
    path("favorites/", views.favorites_list, name="favorites_list"),
    path("poem/<int:poem_id>/favorite/", views.toggle_favorite,
         name="toggle_favorite"),
    path("tools/", views.aythnyk_tools, name="tools"),
    path("poem/<slug:slug>/pdf/", views.download_poem_pdf, name="download_pdf"),
]
