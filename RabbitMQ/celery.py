import os
from celery.schedules import crontab
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RabbitMQ.settings')

app = Celery('RabbitMQ')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


app.conf.beat_schedule = {
    # "raise-future-premiums": {
    #     "task": "apps.payments.tasks.raise_future_premiums",
    #     "schedule": 120 # runs every 2 minutes
    # },
    "salimiana": {
        "task": "notifications.tasks.salimiana",
        "schedule": 10 # runs every 2 minutes
    }
    # "match_policy_premiums_and_scheme_group_premiums": {
    #    "task": "apps.users.tasks.match_policy_premiums_and_scheme_group_premiums",
    #    "schedule": 120 # runs every 2 minutes
    # }
}
