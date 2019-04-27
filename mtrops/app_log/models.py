# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Audit(models.Model):
    host_ip = models.CharField(max_length=32)
    hostname = models.CharField(max_length=64, null=True)
    user_name = models.CharField(max_length=64)
    start_time = models.CharField(max_length=64)
    audit_log = models.TextField()

    def __unicode__(self):
        return self.host_ip
