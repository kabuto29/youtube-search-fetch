from __future__ import absolute_import, unicode_literals
#WIP: will use celery and redis to trigger youtube search api async 
import os
import celery
import django

from celery import Celery
from django.conf import Settings, settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE','youtubeSearch.settings')
django.setup()

app = Celery('sched')

app.conf.beat_schedule = {
    'every-15-sceonds':{
        'task': 'search.tasks.getVideosAuto',
        'schedule' : 15
    }
}

app.config_from_object('django.conf:settings', namespace = 'CELERY')
app.autodiscover_tasks()
app.conf.broker_url = 'redis://127.0.0.1:6379'