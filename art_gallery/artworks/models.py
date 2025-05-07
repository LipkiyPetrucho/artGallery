from django.core.exceptions import ValidationError
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
        "Главное изображение", upload_to="paintings/"
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
    order = models.PositiveIntegerField("Порядок", default=0, blank=False, null=False)

    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"
        ordering = ["order"]

    def __str__(self):
        return self.title

    def get_creation_year(self):
        """Возвращает год создания картины."""
        return self.created_at.year

    def get_absolute_url(self):
        return reverse("artworks:detail", args=[self.id])


class PaintingImage(models.Model):
    painting = models.ForeignKey(
        Painting,
        related_name="extra_images",
        on_delete=models.CASCADE,
        verbose_name="Картина",
    )
    image = models.ImageField("Дополнительный ракурс", upload_to="paintings/")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Доп. изображение"
        verbose_name_plural = "Доп. изображения"

    def clean(self):
        """не даём загрузить > 3 фото для одной картины"""
        if (
                self.painting
                and self.painting.extra_images.exclude(pk=self.pk).count() >= 3
        ):
            raise ValidationError("Можно добавить не более трёх дополнительных фото.")