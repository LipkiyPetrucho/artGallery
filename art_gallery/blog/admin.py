from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "publish", "status")
    list_filter = ("status", "created", "publish", "author")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    raraw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ("status", "publish")
