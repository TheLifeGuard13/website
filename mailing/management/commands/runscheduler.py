from django.core.management.base import BaseCommand

from mailing.scheduler import start_scheduler, start_test_scheduler


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        start_test_scheduler()
