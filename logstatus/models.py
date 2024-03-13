from django.db import models

from clients.models import Client
from letters.models import Letter
from config.settings import NULLABLE


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class LogMessage(models.Model):

    client_email = models.ForeignKey(Client, on_delete=models.SET, verbose_name='Имэйл клиента')
    letter_header = models.ForeignKey(Letter, on_delete=models.SET, verbose_name='Тема письма')
    last_try = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Время последней попытки')
    sending_status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='Статус')
    server_answer = models.TextField(**NULLABLE, verbose_name='Ответ сервера')

    def __str__(self):
        return f'{self.client_email} - {self.sending_status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
