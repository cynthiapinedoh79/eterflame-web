"""
URL configuration for eterpoetic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns   # i18n

urlpatterns = [
    path("api/chat/", include(("chat.urls", "chat"), namespace="chat")),
]

# Translatable, language-prefixed routes
# (prefix_default_language=False keeps / not /en/)

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    # Put blog BEFORE poetry so /blog/ is matched before poetry's <slug:slug>/
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),

    path("about/", include("about.urls")),
    path("", include(("works.urls", "works"), namespace="works")),
    path("aythnyk/", include(("aythnyk.urls", "aythnyk"), namespace="aythnyk")),
    path("aythnyk/", include(("poetry.urls", "poetry"), namespace="poetry")),
    path("aythnyk/songs/", include(("songs.urls", "songs"), namespace="songs")),
    path("aythnyk/shop/", include(("shop.urls", "shop"), namespace="shop")),
    path('', include('facebook_integration.urls')),
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),
    prefix_default_language=False,
)
