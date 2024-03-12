from django.db import models


class Letter(models.Model):

    letter_header = models.CharField(max_length=200, verbose_name='Тема письма')
    letter_body = models.TextField(verbose_name='Тело письма')

    def __str__(self):
        return f'{self.letter_header}'

    class Meta:
        verbose_name = 'письмо'
        verbose_name_plural = 'письма'
