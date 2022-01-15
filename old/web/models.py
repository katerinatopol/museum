from datetime import datetime

from django.db import models


class Publication(models.Model):  # для галереи
    title = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)


class Heroes(models.Model):  # для героев
    title = models.CharField(max_length=256)
    text = models.TextField()
    date = models.DateTimeField(default=datetime.now)
