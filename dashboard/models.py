# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Notes(models.Model):
    body = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(default = datetime.now, blank = True)

    def days_left(self):
        numdays = self.due_date.day - datetime.today().day
        if numdays == 1:
            return "1 day"
        else:
            return str(numdays) + " days"

    def __str__(self):
        return self.body
    class Meta:
        verbose_name_plural = "Note Data"
