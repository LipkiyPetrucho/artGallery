from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from artworks.models import Painting
from blog.models import Post


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['artworks:about', 'artworks:contacts', 'artworks:free_works', 'artworks:gallery']

    def location(self, item):
        return reverse(item)


class PaintingSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Painting.objects.all()

    @staticmethod
    def lastmod(obj):
        return obj.upload_date


class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Post.published.all()

    @staticmethod
    def lastmod(obj):
        return obj.updated
