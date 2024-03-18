import smtplib
from django.utils import timezone

from django.conf import settings
from django.core.mail import send_mail
from logstatus.models import LogMessage
from mailing.models import Mailing


def is_date_in_range(obj):
    now = timezone.localtime(timezone.now())
    if obj.start_datetime < now < obj.end_datetime:
        return True
    return False


def start_mailing(class_obj):
    try:
        server_response = send_mail(
            subject=class_obj.letter.letter_header,
            message=class_obj.letter.letter_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=list(class_obj.client_emails.all().values_list('email', flat=True)),
            fail_silently=False
        )
        LogMessage.objects.create(sending_status=server_response, id_mailing=class_obj)
    except smtplib.SMTPException as e:
        LogMessage.objects.create(sending_status=e, id_mailing=class_obj)


def daily_tasks():
    mailings = Mailing.objects.filter(period="Ежедневно", status="Готовится")
    print(f'Это ежедневные задачи {mailings}')
    if mailings.exists():
        for mailing in mailings:
            start_mailing(mailing)


# def weekly_tasks():
#     mailings = Mailing.objects.filter(period="Еженедельно", status="Готовится")
#     print(f'Это еженедельные задачи {mailings}')
#     if mailings.exists():
#         for mailing in mailings:
#             start_mailing(mailing)


# def monthly_tasks():
#     mailings = Mailing.objects.filter(period="Ежемесячно", status="Готовится")
#     print(f'Это ежемесячные задачи {mailings}')
#     if mailings.exists():
#         for mailing in mailings:
#             start_mailing(mailing)
