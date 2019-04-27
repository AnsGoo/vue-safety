from django.shortcuts import render

# Create your views here.
#coding: utf-8

import re

import json

import os

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect, HttpResponse, Http404

from app_rbac import models as rbacmd

from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from app_rbac import models

from app_cmdb.models import HostInfo

from app_cmdb import models as cmdb_mod

from app_code.models import CodePost

from django.db.models import Sum, Count

import datetime

from mtrops.settings import BASE_DIR

from app_code import models as code_db


# 权限控制装饰器
def Perms_required(func):
    def wrapper(request, *args, **kwargs):
        # 会话权限列表
        perms_list = request.session['perms_list']

        # 请求url处理
        req_url = request.path

        url_list = req_url.strip('#').split('/')

        cur_urls = []
        for i in url_list:
            if re.search('=', i):
                pass
            else:
                cur_urls.append(i)

        cur_url = "/".join(cur_urls)

        # 判断访问url是否存在权限列表中
        if cur_url in perms_list:
            return func(request, *args, **kwargs)
        else:
            return HttpResponse('权限不足')

    return wrapper


@csrf_exempt
def Login(request):
    msg = 'login'
    if request.method == 'POST':
        login_username = request.POST.get('username')
        login_passwd = request.POST.get('passwd')

        user = authenticate(username=login_username, password=login_passwd)

        if user:

            login(request, user)

            request.session['username'] = login_username

            # 获取会话用户角色
            user_role = models.UserInfo.objects.get(user=user).role

            # 获取用户拥有的权限
            perms_list = []

            for perms in user_role.perms.all():

                perms_list.append(perms.perms_url)

            request.session['perms_list'] = perms_list

            # 在权限列表中提取菜单
            menu_one = []
            menu_two = []
            for perms in user_role.perms.all():
                perms_title = perms.perms_title
                perms_type = perms.perms_type
                perms_url = perms.perms_url
                perms_num = perms.perms_num
                pmenu_id = perms.pmenu_id
                perms_icon = perms.perms_icon

                if perms_type == u'一级菜单':
                    menu_one.append({'perms_title': perms_title, 'perms_url': perms_url,
                                     'perms_num': perms_num, 'perms_icon': perms_icon})
                else:
                    menu_two.append({'perms_title': perms_title, 'perms_url': perms_url, 'pmenu_id': pmenu_id,
                                     'perms_num': perms_num})

            # 组成菜单关系列表
            menu_all_list = []
            for i in menu_one:
                perms_num = i['perms_num']
                menu_list = []
                for j in menu_two:
                    pmenu_id = j['pmenu_id']
                    if pmenu_id == perms_num:
                        menu_list.append(j)

                i['menu_two'] = menu_list

                menu_all_list.append(i)

            request.session['menu_all_list'] = menu_all_list

            try:
                # webssh默认登录信息

                user_obj = User.objects.get(username=login_username)

                user_id = user_obj.id

                userinfo_obj = models.UserInfo.objects.get(user_id=user_id)

                userinfo_id = userinfo_obj.id

                login_user_obj = cmdb_mod.LoginUser.objects.get(
                    people_id=userinfo_id)

                username = login_user_obj.login_user

                password = login_user_obj.login_passwd

                publickey = login_user_obj.private_key
            except:
                username = "test"
                password = "123456"
                publickey = None

            if publickey:
                pass
            else:
                publickey = "None"

            data = {"hostname": "127.0.0.1", "port": 22, "username": username,
                    "password": password, "publickey": publickey}

            with open(os.path.join(BASE_DIR + "/" + "hostinfo.json"), 'w') as json_file:

                json.dump(data, json_file, ensure_ascii=False)

            request.session['webssh_info'] = json.dumps(
                data, ensure_ascii=False)

            return redirect('/')

        else:
            msg = "用户名或密码不正确"
            return render(request, "login.html", locals())
    else:
        return render(request, "login.html", locals())


def Logout(request):
    logout(request)
    msg = 'login'
    request.session.delete("username")
    return render(request, "login.html", locals())


@login_required
def Index(request):

    # 时间
    now = datetime.datetime.now()
    A = now.strftime('%A')
    Y = now.strftime('%Y')
    m = now.strftime('%m')
    d = now.strftime('%d')
    H_M = now.strftime('%H:%M')

    # 用户数量
    user_count = User.objects.aggregate(Count('id'))
    user_num = user_count['id__count']

    # 主机数量
    host_count = HostInfo.objects.aggregate(Count('id'))

    host_num = host_count['id__count']

    site_count = CodePost.objects.aggregate(Count('id'))

    site_num = site_count['id__count']

    # 站点更新统计

    site_obj = code_db.Site.objects.all()

    site_title_list = []
    site_pull_count = []
    for i in site_obj:
        site_name = i.site_name
        site_title_list.append(site_name.encode('utf-8'))
        site_id = i.id
        post_site_obj = code_db.CodePost.objects.filter(
            post_site_id=site_id).first()
        try:
            post_site_id = post_site_obj.id
            post_record_count = code_db.PostRecord.objects.filter(
                CodePost_id=post_site_id).count()
            site_pull_count.append(post_record_count)
        except:
            pass

    # 项目代码统计
    project_obj = code_db.Project.objects.all()
    project_title_list = []
    project_site_count = []
    for i in project_obj:
        project_name = i.project_name

        project_title_list.append(project_name.encode("utf-8"))
        project_id = i.id
        site_count = code_db.Site.objects.filter(project_id=project_id).count()
        project_site_count.append(
            {"value": site_count, "name": project_name.encode("utf-8")})

    project_site_count = json.dumps(project_site_count, ensure_ascii=False)

    project_title_list = json.dumps(project_title_list, ensure_ascii=False)

    return render(request, "base.html", locals())


# 修改用户密码
@csrf_exempt
def change_passwd(request):
    if request.method == 'POST':
        current_passwd = request.POST.get("current_passwd")
        new_passwd = request.POST.get("new_passwd")
        username = request.POST.get("username")
        if username:
            pass
        else:
            username = request.session['username']

        user = authenticate(username=username, password=current_passwd)

        if user:
            user.set_password(new_passwd)
            user.save()

            msg = "密码已修改,请重新登录"
        else:
            msg = "当前密码不正确"

        return HttpResponse(msg)
    else:
        return HttpResponse("未知请求")
