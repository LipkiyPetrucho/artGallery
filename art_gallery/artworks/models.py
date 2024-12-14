from django.db import models
from django.urls import reverse


class Painting(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "available", "Доступно"
        SOLD = "sold", "Продано"
        RESERVED = "reserved", "Зарезервировано"

    # TODO: author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField("Название", max_length=200)
    created_at = models.DateField("Дата создания", blank=True, null=True)
    upload_date = models.DateTimeField("Дата загрузки", auto_now_add=True)
    material = models.CharField("Материал", max_length=100)
    dimensions = models.CharField("Размеры", max_length=50)
    image = models.ImageField(
        "Изображение", upload_to="paintings/"
    )  # TODO:   /%Y/%m/%d/
    description = models.TextField("Описание", blank=True)
    category = models.CharField("Категория", max_length=100, blank=True, null=True)
    # TODO: tags = models.CharField(max_length=200, blank=True)
    # TODO: price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.AVAILABLE,
        verbose_name="Статус",
    )

    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"

    def __str__(self):
        return self.title

    def get_creation_year(self):
        """Возвращает год создания картины."""
        return self.created_at.year

    def get_absolute_url(self):
        return reverse("artworks:detail", args=[self.id])
