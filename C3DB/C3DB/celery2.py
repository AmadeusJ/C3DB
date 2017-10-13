from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chemdb.settings')

app = Celery('chemdb', broker='redis://')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.broker_url = 'redis://localhost:6379/0'
app.conf.result_backend = 'redis://localhost:6379/0'

@app.task(bind=True)
def debug_task(self):
    print 'Request: {0!r}'.format(self.request)
