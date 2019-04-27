# coding:utf-8

from __future__ import absolute_import

from celery import task

from celery import shared_task

from app_cmdb import sysinfo

from app_cmdb import models


@shared_task
def SyncHost_job(ips):
    data = sysinfo.main(ips)
    for ip in data.keys():
        host_obj = models.HostInfo.objects.get(IP=ip)

        sys_info = data[ip]

        host_obj.hostname = sys_info['localhost']
        host_obj.os_type = sys_info['kernel']
        host_obj.service_type = sys_info['productname']
        host_obj.os_version = sys_info['os'] + ' ' + sys_info['osrelease']
        host_obj.mem_total = sys_info['mem_total']
        host_obj.mem_swap = sys_info['SwapTotal']
        host_obj.cpu_type = sys_info['cpu_model']
        host_obj.cpu_num = sys_info['num_cpus']
        host_obj.mount_home = sys_info['/home']
        host_obj.mount_root = sys_info['/']
        host_obj.mount_alidata = sys_info['/alidata']
        host_obj.kernel = sys_info['kernel'] + ' ' + sys_info['kernelrelease']
        host_obj.status = 'up'
        host_obj.save()

    return u"已同步"
