from django.db import models
from django.contrib.postgres.fields import JSONField

class videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=5000)
    publishedat = models.DateTimeField()
    thumbnails = JSONField()
