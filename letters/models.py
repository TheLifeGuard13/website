from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Letter(models.Model):
    """
    Модель Письма
    """

    letter_header = models.CharField(max_length=200, verbose_name="Тема письма")
    letter_body = models.TextField(verbose_name="Тело письма")
    created_at = models.DateField(**NULLABLE, auto_now_add=True, verbose_name="Дата создания")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец")

    def __str__(self) -> str:
        return f"{self.letter_header}"

    class Meta:
        verbose_name = "письмо"
        verbose_name_plural = "письма"
