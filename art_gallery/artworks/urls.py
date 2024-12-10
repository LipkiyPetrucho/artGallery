from django.urls import path
from .views import (
    about_view,
    gallery_view,
    contacts_view,
    painting_detail,
    free_works,
)

app_name = "artworks"

urlpatterns = [
    path("about/", about_view, name="about"),
    path("gallery/", gallery_view, name="gallery"),
    path("free-works/", free_works, name="free_works"),
    path("painting/<int:id>/", painting_detail, name="detail"),
    path("contacts/", contacts_view, name="contacts"),
]
