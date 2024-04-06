from django.db import models

from config import settings
from config.settings import NULLABLE


class Letter(models.Model):

    letter_header = models.CharField(max_length=200, verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')
    created_at = models.DateField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец')

    def __str__(self):
        return f'{self.letter_header}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
