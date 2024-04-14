from django.conf import settings
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email=settings.SUPERUSER_EMAIL,
            first_name=settings.SUPERUSER_FIRST_NAME,
            last_name=settings.SUPERUSER_LAST_NAME,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password(settings.SUPERUSER_PASSWORD)
        user.save()
