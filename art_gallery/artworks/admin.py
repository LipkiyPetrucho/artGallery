from django.contrib import admin

from .models import Painting


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "material",
        "dimensions",
        "image",
        "description",
    ]
    list_filter = ["upload_date"]
    search_fields = (
        "title",
        "description",
        "material",
        "category",
    )
