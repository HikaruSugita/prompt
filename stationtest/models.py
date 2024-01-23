# prompt/models.py
from django.conf import settings
from django.db import models
from django.utils import timezone

class Stationtest(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prompt = models.TextField()
    posted_date = models.DateTimeField(default=timezone.now)