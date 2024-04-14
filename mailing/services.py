import smtplib

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from logstatus.models import LogMessage


def start_mailing(class_obj):
    try:
        send_mail(
            subject=class_obj.letter.letter_header,
            message=class_obj.letter.letter_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=list(class_obj.client_emails.all().values_list("email", flat=True)),
            fail_silently=False,
        )
        LogMessage.objects.create(sending_status="Успешно", id_mailing=class_obj)
    except smtplib.SMTPException as e:
        LogMessage.objects.create(sending_status="Безуспешно", id_mailing=class_obj)
