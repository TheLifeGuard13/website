from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    help = "Download fixtures to files from all apps"

    def handle(self, *args, **options):
        call_command("dumpdata", "auth", "-o", "website/fixtures/auth_data.json")
        call_command("dumpdata", "users", "-o", "website/fixtures/users_data.json")
        call_command("dumpdata", "blog", "-o", "website/fixtures/blog_data.json")
        call_command("dumpdata", "clients", "-o", "website/fixtures/clients_data.json")
        call_command("dumpdata", "letters", "-o", "website/fixtures/letters_data.json")
        call_command("dumpdata", "mailing", "-o", "website/fixtures/mailing_data.json")
        call_command("dumpdata", "logstatus", "-o", "website/fixtures/logstatus_data.json")
