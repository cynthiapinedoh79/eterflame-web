"""
URL configuration for eterflame project.

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
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from core.sitemaps import sitemaps
from django.conf.urls.i18n import i18n_patterns   # i18n
from django.http import Http404

handler404 = 'django.views.defaults.page_not_found'


def trigger_404(request):
    raise Http404


urlpatterns = [
    path("api/chat/", include(("chat.urls", "chat"), namespace="chat")),
    path("test-404/", trigger_404),
    # SEO: sitemap and robots — NOT inside i18n_patterns (must be at root)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
    # PWA: manifest and service worker served at root
    path('manifest.json', TemplateView.as_view(template_name='manifest.json', content_type='application/manifest+json'), name='pwa_manifest'),
    path('sw.js', TemplateView.as_view(template_name='sw.js', content_type='application/javascript'), name='pwa_sw'),
    # Audience: newsletter subscription endpoint (no i18n needed)
    path('aythnyk/subscribe/', include(('audience.urls', 'audience'), namespace='audience')),
]

# Translatable, language-prefixed routes
# (prefix_default_language=False keeps / not /en/)

urlpatterns += i18n_patterns(
    path("admin/", admin.site.urls),
    # Put blog BEFORE poetry so /blog/ is matched before poetry's <slug:slug>/
    path("blog/", include(("blog.urls", "blog"), namespace="blog")),

    path("about/", include("about.urls")),
    path("", include(("works.urls", "works"), namespace="works")),
    path("works/design/", include(("design_app.urls", "design"), namespace="design")),
    path("works/media/", include(("media_app.urls", "media"), namespace="media")),
    path("works/studio/", include(("studio_app.urls", "studio"), namespace="studio")),
    path("aythnyk/", include(("aythnyk.urls", "aythnyk"), namespace="aythnyk")),
    path("aythnyk/", include(("poetry.urls", "poetry"), namespace="poetry")),
    path("aythnyk/songs/", include(("songs.urls", "songs"), namespace="songs")),
    path("aythnyk/shop/", include(("shop.urls", "shop"), namespace="shop")),
    path('', include('facebook_integration.urls')),
    path("accounts/", include("allauth.urls")),
    path("summernote/", include("django_summernote.urls")),
    prefix_default_language=False,
)
