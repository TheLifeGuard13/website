from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    # def ready(self):
    #     from mailing.scheduler import start_scheduler
    #     sleep(3)
    #     start_scheduler()
