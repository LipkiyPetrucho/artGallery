from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.static import serve

from artworks.views import home_view
from sitemap import StaticViewSitemap, PaintingSitemap, PostSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'paintings': PaintingSitemap,
    'posts': PostSitemap,
}

urlpatterns = [
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("artworks/", include("artworks.urls")),
    path("blog/", include("blog.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('google1234567890abc.html', serve, {'document_root': settings.STATIC_ROOT, 'path': 'google1234567890abc.html'}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
