from django.db import models
from django.urls import reverse


class Painting(models.Model):
    # TODO: STATUS_CHOICES = [
    #     ('available', 'Available'),
    #     ('sold', 'Sold'),
    #     ('reserved', 'Reserved'),]
    # TODO: author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    created_at = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)
    material = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=50)
    image = models.ImageField(upload_to="paintings/")  # TODO:   /%Y/%m/%d/
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    # TODO: tags = models.CharField(max_length=200, blank=True)
    # TODO: price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # TODO: status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.title

    def get_creation_year(self):
        """Возвращает год создания картины."""
        return self.created_at.year

    def get_absolute_url(self):
        return reverse("artworks:detail", args=[self.id])
