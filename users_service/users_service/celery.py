import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'users_service.settings')

app = Celery('users_service')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = True

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
