from django.db import models

from django.contrib.auth.models import User
from app_rbac.models import UserInfo

# Create your models here.


class HostGroup(models.Model):
    group_name = models.CharField(max_length=64, unique=True)
    msg = models.CharField(max_length=128, null=True)

    def __unicode__(self):
        return self.group_name


class IDC(models.Model):
    idc_name = models.CharField(max_length=64, unique=True)
    msg = models.CharField(max_length=128, null=True)


class LoginUser(models.Model):
    login_user = models.CharField(max_length=64, unique=True)
    login_passwd = models.CharField(max_length=256)
    people = models.ForeignKey(to=UserInfo, on_delete=None)
    private_key = models.CharField(max_length=2048, null=True)

    def __unicode__(self):
        return self.login_user


class HostInfo(models.Model):
    IP = models.CharField(max_length=64, unique=True)
    remote_user = models.ForeignKey(
        to="LoginUser", on_delete=models.CASCADE, default='1')
    device_type = models.CharField(max_length=64)
    idc = models.ForeignKey(to='IDC', on_delete=models.CASCADE)
    port = models.CharField(max_length=64)
    host_group = models.ForeignKey(to='HostGroup', on_delete=models.CASCADE)
    msg = models.CharField(max_length=64, null=True)
    hostname = models.CharField(max_length=64, null=True)
    in_ip = models.CharField(max_length=64, null=True)
    os_type = models.CharField(max_length=64, null=True)
    service_type = models.CharField(max_length=64, null=True)
    os_version = models.CharField(max_length=64, null=True)
    mem_total = models.CharField(max_length=64, null=True)
    mem_swap = models.CharField(max_length=32, default="0")
    cpu_type = models.CharField(max_length=64, null=True)
    cpu_num = models.CharField(max_length=16, null=True)
    mount_home = models.CharField(max_length=128, null=True)
    mount_root = models.CharField(max_length=128, null=True)
    mount_alidata = models.CharField(max_length=128, null=True)
    kernel = models.CharField(max_length=64, null=True)
    status = models.CharField(max_length=16, null=True)
    addTime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.IP
