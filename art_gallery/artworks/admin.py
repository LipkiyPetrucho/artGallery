from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from .admin_forms import PaintingAdminForm
from .models import Painting, PaintingImage


class PaintingImageInline(admin.TabularInline):
    model = PaintingImage
    extra = 3  # покажем ровно три пустых поля
    max_num = 3  # запретим добавить больше
    fields = ("image", "order",)


@admin.register(Painting)
class PaintingAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = PaintingAdminForm
    inlines = (PaintingImageInline,)
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
    ordering = ("order",)
