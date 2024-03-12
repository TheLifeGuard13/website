from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):

    email = models.EmailField(verbose_name='Имэйл клиента')
    name = models.CharField(max_length=150, verbose_name='ФИО клиента')
    comment = models.TextField(**NULLABLE, verbose_name='Комментарий')
    avatar = models.ImageField(**NULLABLE, upload_to='clients/', verbose_name='Аватар')
    created_at = models.DateField(**NULLABLE, auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.email} ({self.name})'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
