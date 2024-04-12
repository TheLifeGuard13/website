from datetime import datetime, timedelta

from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django.utils import timezone

from mailing.models import Mailing
from mailing.services import start_mailing


def filter_mailing(obj):
    now = timezone.localtime(timezone.now())

    if obj.start_datetime < now < obj.end_datetime:

        if not obj.next_sending_time:
            print(0)

            if obj.first_sending_time >= now:
                obj.next_sending_time = obj.first_sending_time
                print(1)
            else:
                if now.time() > obj.first_sending_time.time():
                    obj.next_sending_time = datetime.combine(now.date() + timedelta(days=1), obj.first_sending_time.time())
                    print(2)
                print(obj.first_sending_time)
                obj.next_sending_time = datetime.combine(now.date(), obj.first_sending_time.time())
                print(3)
            print(4)
            obj.save()

        elif now > obj.next_sending_time > obj.start_datetime:
            print(6)
            start_mailing(obj)
            obj.status = "Запущена"
            if obj.period == "Ежедневно":
                obj.next_sending_time = now + timedelta(days=1)
                print(7)
            elif obj.period == "Еженедельно":
                obj.next_sending_time = now + timedelta(weeks=1)
                print(8)
            elif obj.period == "Ежемесячно":
                obj.next_sending_time = now + timedelta(days=30)
                print(9)
            print(10)
            obj.save()
        print(12)

    elif now > obj.end_datetime:
        obj.status = "Завершена"
        print(11)
        obj.save()


def sending_tasks():
    mailings = Mailing.objects.filter(status__in=["Создана", "Запущена"])
    if mailings.exists():
        for mailing in mailings:
            print(mailing.name)
            filter_mailing(mailing)


def start_scheduler():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    print("Starting scheduler...")

    scheduler.add_job(sending_tasks, trigger=CronTrigger(minute='*/1'), id="sending_tasks",
                      max_instances=1, replace_existing=True)

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown(wait=False)
