# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils import timezone

class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

    def __str__(self):
        return str(self.docfile)

