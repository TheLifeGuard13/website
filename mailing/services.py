import smtplib

from django.conf import settings
from django.core.mail import send_mail

from logstatus.models import LogMessage


def start_mailing(subject, message, email_list, mailing):
    try:
        server_response = send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=email_list,
            fail_silently=False
        )
        LogMessage.objects.create(sending_status=server_response, id_mailing=mailing)
    except smtplib.SMTPException as e:
        LogMessage.objects.create(sending_status=e, id_mailing=mailing)
