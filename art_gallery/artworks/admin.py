from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .admin_forms import PaintingAdminForm
from .models import Painting


@admin.register(Painting)
class PaintingAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = PaintingAdminForm
    list_display = [
        "title",
        "material",
        "dimensions",
        "image",
        "description",
        "status",
        "order",
    ]
    list_filter = ["upload_date", "status"]
    search_fields = (
        "title",
        "description",
        "material",
        "category",
    )
    list_editable = ("status",)
    ordering = ("-upload_date",)
