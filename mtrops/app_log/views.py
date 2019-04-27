# -*- coding: utf-8 -*-


import json

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app_auth.views import Perms_required
from app_log import models


@login_required
@Perms_required
def ELK(request):
    return redirect('http://192.168.1.88:5601/')


@login_required
@Perms_required
def audit(request):
    title = "操作审计"
    audit_obj = models.Audit.objects.all().order_by("-start_time")
    audit_list = []
    for i in audit_obj:
        audit_list.append({'host_ip': i.host_ip, 'hostname': i.hostname,
                           'user_name': i.user_name, 'start_time': i.start_time, 'audit_id': i.id})
    return render(request, "log_audit.html", locals())


@csrf_exempt
def audit_check(request):
    if request.method == "POST":
        audit_id = request.POST.get('audit_id')
        audit_obj = models.Audit.objects.get(id=audit_id)
        audit_log = audit_obj.audit_log
        return HttpResponse(audit_log)
