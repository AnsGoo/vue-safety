# coding:utf-8
from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Role(models.Model):
    role_title = models.CharField(max_length=64, unique=True)
    role_msg = models.CharField(max_length=128, null=True)
    perms = models.ManyToManyField(to="Permission")

    def __unicode__(self):
        return self.role_title


class UserInfo(models.Model):
    user = models.OneToOneField(User, default=2, on_delete=models.CASCADE)
    role = models.ForeignKey(to="Role", on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=128, null=True)
    status = models.CharField(max_length=64, default='离线')

    def __unicode__(self):
        return self.username


class Permission(models.Model):
    perms_title = models.CharField(max_length=64)
    perms_url = models.CharField(max_length=64)
    perms_type = models.CharField(max_length=32)
    pmenu_id = models.CharField(max_length=32, null=True)
    perms_num = models.CharField(max_length=32, null=True)
    perms_icon = models.CharField(max_length=256, null=True)

    def __unicode__(self):
        return self.perms_title
