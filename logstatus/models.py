from django.db import models

from config.settings import NULLABLE
from mailing.models import Mailing


class LogMessage(models.Model):
    SENT = "Успешно"
    FAIL = "Безуспешно"

    LOG_CHOICES = {
        SENT: 'Успешно',
        FAIL: 'Безуспешно',
    }

    id_mailing = models.ForeignKey(Mailing, **NULLABLE, on_delete=models.CASCADE, verbose_name='Рассылка')
    last_try = models.DateTimeField(**NULLABLE, auto_now_add=True, verbose_name='Время последней попытки')
    sending_status = models.CharField(max_length=10, choices=LOG_CHOICES, verbose_name='Логстатус')

    def __str__(self):
        return f'{self.last_try}, {self.id_mailing}, {self.sending_status}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
