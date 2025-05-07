from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin

from .admin_forms import ExhibitionAdminForm
from .models import Exhibition, VideoItem


@admin.register(Exhibition)
class ExhibitionAdmin(SortableAdminMixin, admin.ModelAdmin):
    form = ExhibitionAdminForm
    list_display = ('date', 'title', 'venue', 'order')
    list_editable = ('order',)


@admin.register(VideoItem)
class VideoItemAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('caption', 'embed_url', 'order')
    list_editable = ('order',)
