from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from artworks.views import home_view

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),
    path("artworks/", include("artworks.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
