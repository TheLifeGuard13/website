from django.db import models

from clients.models import Client
from config.settings import NULLABLE
from letters.models import Letter


class Period(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название периода')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'период'
        verbose_name_plural = 'периоды'


class Mailing(models.Model):

    name = models.CharField(max_length=150, verbose_name='Имя рассылки')
    client_emails = models.ManyToManyField(Client)
    letter_header = models.ForeignKey(Letter, **NULLABLE, on_delete=models.SET, verbose_name='Тема письма')
    sending_time = models.DateTimeField(**NULLABLE, verbose_name='Время рассылки')
    period = models.ForeignKey(Period, on_delete=models.CASCADE, verbose_name='Период')
    start_datetime = models.DateTimeField(**NULLABLE, verbose_name='Время начала')
    end_datetime = models.DateTimeField(**NULLABLE, verbose_name='Время конца')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
