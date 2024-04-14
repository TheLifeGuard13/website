from django.conf import settings
from django.db import models

from config.settings import NULLABLE


class Client(models.Model):

    email = models.EmailField(verbose_name="Имэйл клиента")
    name = models.CharField(max_length=150, verbose_name="ФИО клиента")
    comment = models.TextField(**NULLABLE, verbose_name="Комментарий")
    avatar = models.ImageField(**NULLABLE, upload_to="clients/", verbose_name="Аватар")
    created_at = models.DateField(**NULLABLE, auto_now_add=True, verbose_name="Дата создания")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, default="", on_delete=models.CASCADE, **NULLABLE, verbose_name="Владелец"
    )

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
