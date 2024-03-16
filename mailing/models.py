from django.db import models

from clients.models import Client
from config.settings import NULLABLE
from letters.models import Letter

PERIOD_CHOICES = {
    'Ежедневно': 'Ежедневно',
    'Еженедельно': 'Еженедельно',
    'Ежемесячно': 'Ежемесячно'
}

STATUS_CHOICES = {
    'Готовится': 'Готовится',
    'Успешно': 'Успешно',
    'Безуспешно': 'Безуспешно'
}


class Mailing(models.Model):

    name = models.CharField(max_length=150, verbose_name='Имя рассылки')
    client_emails = models.ManyToManyField(Client, verbose_name='Имэйлы')
    letter = models.ForeignKey(Letter, **NULLABLE, on_delete=models.SET, verbose_name='Письмо')
    sending_time = models.TimeField(**NULLABLE, verbose_name='Время рассылки')
    period = models.CharField(max_length=150, choices=PERIOD_CHOICES, verbose_name='Период')
    start_datetime = models.DateTimeField(**NULLABLE, verbose_name='Время начала')
    end_datetime = models.DateTimeField(**NULLABLE, verbose_name='Время конца')
    created_at = models.DateField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
