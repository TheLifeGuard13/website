from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore

from mailing.models import Mailing
from mailing.services import start_mailing


def daily_tasks(some_func):
    start_mailing(some_func())


def new_func():
    mailings = Mailing.objects.filter(period="Ежедневно", status="Готовится")
    print(f'Это ежедневные задачи {mailings}')
    if mailings.exists():
        for mailing in mailings:
            return mailing


def start_scheduler():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    print("Starting scheduler...")

    scheduler.add_job(
        daily_tasks,
        trigger=CronTrigger(start_date=new_func().start_datetime, end_date=new_func().end_datetime),
        args=[new_func],
        id="daily_tasks",
        max_instances=2,
        replace_existing=True,
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown(wait=False)
