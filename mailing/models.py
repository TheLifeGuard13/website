from django.db import models

from clients.models import Client
from config import settings
from config.settings import NULLABLE
from letters.models import Letter


class Mailing(models.Model):
    DAILY = "Ежедневно"
    WEEKLY = "Еженедельно"
    MONTHLY = "Ежемесячно"

    PERIOD_CHOICES = {
        DAILY: 'Ежедневно',
        WEEKLY: 'Еженедельно',
        MONTHLY: 'Ежемесячно'
    }

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = {
        CREATED: 'Создана',
        STARTED: 'Запущена',
        COMPLETED: 'Завершена'
    }

    name = models.CharField(max_length=150, verbose_name='Имя рассылки')
    client_emails = models.ManyToManyField(Client, verbose_name='Имэйлы')
    letter = models.ForeignKey(Letter, **NULLABLE, on_delete=models.SET, verbose_name='Письмо')
    first_sending_time = models.DateTimeField(**NULLABLE, verbose_name='Время первой рассылки')
    period = models.CharField(max_length=150, choices=PERIOD_CHOICES, verbose_name='Период')
    start_datetime = models.DateTimeField(**NULLABLE, verbose_name='Время начала')
    end_datetime = models.DateTimeField(**NULLABLE, verbose_name='Время конца')
    created_at = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Время создания')
    status = models.CharField(default='Создана', max_length=20, **NULLABLE, choices=STATUS_CHOICES, verbose_name='Статус')

    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='Владелец')

    def __str__(self):
        return (f'{self.name}, {self.client_emails}, {self.letter},'
                f'{self.start_datetime}, {self.end_datetime}, {self.created_at},'
                f'{self.first_sending_time}, {self.period}, {self.status}, {self.pk}')

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

        permissions = [('set_inactive', 'Can block mailing')]
