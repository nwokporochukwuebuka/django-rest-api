from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


# setup 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api_project.settings')

app = Celery('django_api_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()