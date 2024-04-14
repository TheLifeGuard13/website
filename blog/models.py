from django.conf import settings
from django.db import models


class Blog(models.Model):
    """
    Модель Блога
    """

    header = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(null=True, blank=True, verbose_name="Содержимое")
    preview = models.ImageField(upload_to="blogs/", null=True, blank=True, verbose_name="Изображение")
    views_count = models.IntegerField(default=0, verbose_name="Просмотры")
    published_at = models.DateField(null=True, blank=True, auto_now_add=True, verbose_name="Дата публикации")

    slug = models.CharField(max_length=100, null=True, blank=True, verbose_name="Читабельная ссылка")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Владелец")

    def __str__(self) -> str:
        return f"{self.header}, {self.description}"

    class Meta:
        verbose_name = "запись"
        verbose_name_plural = "записи"
