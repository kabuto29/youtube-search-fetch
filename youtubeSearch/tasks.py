from celery.app import shared_task
from youtubeSearch.celery import app

@shared_task
def hellow_celery(something):
    print("hello celery to {}".format(something))