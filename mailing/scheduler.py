from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from django_apscheduler.jobstores import DjangoJobStore

from mailing.services import daily_tasks


def start_scheduler():
    scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), "default")
    print("Starting scheduler...")

    scheduler.add_job(
        daily_tasks,
        trigger=CronTrigger(second="*/30"),
        id="daily_tasks",
        max_instances=1,
        replace_existing=True,
    )

    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown(wait=False)
