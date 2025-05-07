from django.db import models


class Exhibition(models.Model):
    date = models.DateField("Дата выставки")
    title = models.CharField("Название", max_length=200)
    venue = models.CharField("Место проведения", max_length=200)
    order = models.PositiveIntegerField("Порядок вывода", default=0)

    class Meta:
        ordering = ['order',]
        verbose_name = "Выставка"
        verbose_name_plural = "Выставки"

    def __str__(self):
        return f"{self.date:%B %Y} – {self.title}"


class VideoItem(models.Model):
    embed_url = models.URLField("URL для <iframe> или видеофайл")
    caption = models.CharField("Подпись", max_length=200, blank=True)
    order = models.PositiveIntegerField("Порядок вывода", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Видео для About"
        verbose_name_plural = "Видео для About"

    def __str__(self):
        return self.caption or self.embed_url