# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app_auth.views import Perms_required
from mtrops.settings import BASE_DIR
import json
import os
import datetime
import shutil
from app_sys import salt_cp_file
from app_cmdb import models as cmdb_mod
from django.contrib.auth.models import User
from app_rbac.models import UserInfo

import time
import hmac
import hashlib
import json


@login_required
@Perms_required
def Nessus(request):
    return redirect('https://39.108.231.212:8834/')


# 上传文件
@csrf_exempt
@login_required
@Perms_required
def Upfile(request):
    if request.method == "POST":
        path = request.POST.get("path")
        upfile = request.FILES.get("upfile")
        ip = request.POST.get("ip")

        up_file_path = os.path.join(BASE_DIR, 'static', 'upload', ip)

        if os.path.exists(up_file_path):
            pass
        else:
            os.makedirs(up_file_path)

        file_path = os.path.join(up_file_path, upfile.name)

        src = "salt://"+file_path

        dest = path.rstrip("/")+"/"+upfile.name

        if os.path.exists(file_path):
            date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            os.rename(file_path, file_path+"_"+date_str)
        else:
            pass

        f = open(file_path, 'wb')

        for chunk in upfile.chunks():
            f.write(chunk)
        f.close()

        result = salt_cp_file.upfile(ip, src, dest)

        if result[ip]:
            msg = "上传成功"
        else:
            msg = "上传失败"
        return HttpResponse(msg)
    else:
        return HttpResponse("未知请求")


# 下载文件
@csrf_exempt
@login_required
@Perms_required
def Downfile(request):
    if request.method == "POST":
        path = request.POST.get("path")
        ip = request.POST.get("ip")
        result = salt_cp_file.downfile(ip, path)

        if result[ip]:
            salt_file_path = "/var/cache/salt/master/minions/%s/files" % ip
            salt_push_file = salt_file_path + path
            downfile_path = os.path.join(BASE_DIR, 'static', 'download', ip)

            if os.path.exists(downfile_path):
                pass
            else:
                os.makedirs(downfile_path)

            file_name = path.split("/")[-1]

            salt_file = salt_file_path + path

            save_file = downfile_path + "/" + file_name

            if os.path.exists(save_file):
                date_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
                os.rename(save_file, save_file + "_" + date_str)
            else:
                pass
            shutil.move(salt_file, save_file)

            msg = "http://192.168.1.218:8080/static/download/%s/%s" % (
                ip, file_name)
        else:
            msg = "下载失败，请检查文件是否存在"

        return HttpResponse(msg)
    else:
        return HttpResponse("未知请求")


@login_required
# @Perms_required
def GateOne(request):
    title = "GateOne"

    username = request.session['username']

    user_obj = User.objects.get(username=username)

    user_id = user_obj.id

    userinfo_obj = UserInfo.objects.get(user_id=user_id)

    userinfo_id = userinfo_obj.id

    login_user_obj = cmdb_mod.LoginUser.objects.filter(
        people_id=userinfo_id).first()

    login_user = login_user_obj.login_user

    return render(request, "sys_gateone.html", locals())


'''
@csrf_exempt
@login_required
@Perms_required
def Webssh(request):

    title = "webssh"

    if request.method == "POST":
        hostname = request.POST.get('ip')
        hostinfo_obj = cmdb_mod.HostInfo.objects.get(IP=hostname)
        port = hostinfo_obj.port

        webssh_info =  json.loads(request.session['webssh_info'])

        webssh_info["hostname"] = hostname

        webssh_info["port"] = port


        with open(os.path.join(BASE_DIR+"/"+"hostinfo.json"), 'w') as json_file:

            json.dump(webssh_info, json_file, ensure_ascii=False)

        json_file.close()

        return HttpResponse("con")

    else:
        hostgroup_obj = cmdb_mod.HostGroup.objects.all()
        tree_info = []

        for i in hostgroup_obj:
            hostgroup_id = i.id
            hostgroup_name = i.group_name
            hostinfo_obj = cmdb_mod.HostInfo.objects.filter(host_group_id=hostgroup_id)
            tree_info.append({"id":hostgroup_id, "pId":0, "name":hostgroup_name, "open":"true"})

            for j in hostinfo_obj:
                host_id = j.id
                host_ip =  j.IP
                id = hostgroup_id*10+host_id

                if j.os_type=="Windows":
                    pass
                else:
                    tree_info.append({"id": id, "pId": hostgroup_id, "name": host_ip})

        data =  json.dumps(tree_info,ensure_ascii=False)

        info = {}
        with open(os.path.join(BASE_DIR+"/"+"hostinfo.json"), 'r') as json_file:
            info = json.load(json_file)
        json_file.close()

        return render(request,"sys_webssh.html",locals())
'''
