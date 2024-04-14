from datetime import timedelta, datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.utils import timezone
from django_apscheduler.jobstores import DjangoJobStore

from mailing.models import Mailing
from mailing.services import start_mailing


def filter_mailing(obj):
    now = timezone.localtime(timezone.now())
    print(now)
    if obj.start_datetime < now < obj.end_datetime:

        if not obj.next_sending_time:
            if obj.first_sending_time >= now:
                obj.next_sending_time = obj.first_sending_time
            else:
                if now.time() > obj.first_sending_time.time():
                    obj.next_sending_time = datetime.combine(
                        now.date() + timedelta(days=1), obj.first_sending_time.time()
                    )
                obj.next_sending_time = datetime.combine(now.date(), obj.first_sending_time.time())
            obj.save()

        elif now > obj.next_sending_time > obj.start_datetime:
            start_mailing(obj)
            obj.status = "Запущена"
            if obj.period == "Ежедневно":
                obj.next_sending_time = now + timedelta(days=1)
            elif obj.period == "Еженедельно":
                obj.next_sending_time = now + timedelta(weeks=1)
            elif obj.period == "Ежемесячно":
                obj.next_sending_time = now + timedelta(days=30)
            obj.save()

    elif now > obj.end_datetime:
        obj.status = "Завершена"
        obj.save()


def sending_tasks():
    mailings = Mailing.objects.filter(status__in=["Создана", "Запущена"])
    if mailings.exists():
        for mailing in mailings:
            if mailing.is_active:
                filter_mailing(mailing)


def start_scheduler():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    print("Starting scheduler...")

    scheduler.add_job(
        sending_tasks, trigger=CronTrigger(minute="*/1"), id="sending_tasks", max_instances=1, replace_existing=True
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown(wait=False)
