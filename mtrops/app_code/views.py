# coding:utf-8


import json
# import commands
import time
import re
import os
from django.shortcuts import render, HttpResponse
from app_code import models
from app_cmdb.models import HostInfo, HostGroup
from django.db.models import Q
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from app_auth.views import Perms_required
from mtrops.settings import BASE_DIR
from app_code import salt_script


@login_required
@Perms_required
def Project(request):
    project_info = models.Project.objects.all()
    project_list = []
    for project in project_info:
        project_name = project.project_name
        project_msg = project.project_msg
        project_id = project.id
        project_list.append({'project_name': project_name,
                             'project_msg': project_msg, 'project_id': project_id})
    return render(request, "code_project.html", {'title': '项目管理', 'project_list': project_list})


@csrf_exempt
@login_required
@Perms_required
def AddProject(request):
    if request.method == 'POST':
        project_name = request.POST.get('project_name')
        project_msg = request.POST.get('project_msg')
        try:
            project_obj = models.Project(
                project_name=project_name, project_msg=project_msg)
            project_obj.save()
            return HttpResponse('添加成功')
        except:
            return HttpResponse('添加失败')
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def EditProject(request):
    if request.method == "POST":
        project_name = request.POST.get("project_name")
        project_msg = request.POST.get("project_msg")
        project_id = request.POST.get("project_id")
        action = request.POST.get("action", None)
        if action:
            project_obj = models.Project.objects.get(id=project_id)
            project_obj.project_name = project_name
            project_obj.project_msg = project_msg
            project_obj.save()
            return HttpResponse("修改成功")
        else:
            project_info = models.Project.objects.get(id=project_id)
            info_json = {'project_id': project_info.id,
                         'project_name': project_info.project_name, 'project_msg': project_info.project_msg}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelProject(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id")

        models.Project.objects.get(id=project_id).delete()

        return HttpResponse("已删除")


@login_required
@Perms_required
def Site(request):
    project_info = models.Project.objects.all()
    project_list = []
    for project in project_info:
        project_name = project.project_name
        project_id = project.id
        project_list.append(
            {'project_name': project_name, 'project_id': project_id})

    depend_obj = models.Depend.objects.all()
    depend_list = []

    for depend in depend_obj:
        depend_name = depend.depend_name
        depend_list.append(depend_name)

    site_info = models.Site.objects.all()
    site_list = []

    for site in site_info:
        site_id = site.id
        site_name = site.site_name
        site_msg = site.site_msg
        site_project = site.project

        site_url = site.site_url
        site_depend = site.site_depend

        site_list.append({'site_name': site_name, 'site_msg': site_msg, 'site_project': site_project,
                          'site_url': site_url, 'site_depend': site_depend, 'site_id': site_id})

    return render(request, "code_site.html", {'title': '站点管理', 'site_list': site_list, 'project_list': project_list, 'depend_list': depend_list})


@csrf_exempt
@login_required
@Perms_required
def AddSite(request):
    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        site_msg = request.POST.get('site_msg')
        site_project = request.POST.get('site_project')
        site_url = request.POST.get('site_url')
        site_depend = request.POST.get('site_depend')
        site_depend = json.loads(site_depend)
        site_depend = sorted(site_depend)
        site_depend = '/'.join(site_depend)
        try:
            site_obj = models.Site(site_name=site_name, site_msg=site_msg, project_id=site_project, site_url=site_url,
                                   site_depend=site_depend)
            site_obj.save()
            return HttpResponse('添加成功')
        except:
            return HttpResponse('添加失败')
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def EditSite(request):
    if request.method == "POST":
        site_id = request.POST.get("site_id")
        site_name = request.POST.get('site_name')
        site_msg = request.POST.get('site_msg')
        site_project = request.POST.get('site_project')
        site_url = request.POST.get('site_url')
        site_depend = request.POST.get('site_depend')
        action = request.POST.get("action", None)
        if action:
            site_depend = json.loads(site_depend)
            site_depend = sorted(site_depend)
            site_depend = '/'.join(site_depend)
            site_obj = models.Site.objects.get(id=site_id)
            site_obj.site_name = site_name
            site_obj.site_msg = site_msg
            site_obj.project_id = site_project
            site_obj.site_url = site_url
            site_obj.site_depend = site_depend
            site_obj.save()
            return HttpResponse("修改成功")
        else:
            site_info = models.Site.objects.get(id=site_id)
            info_json = {'site_id': site_info.id, 'site_name': site_info.site_name, 'site_msg': site_info.site_msg,
                         'site_project': site_info.project_id, 'site_url': site_info.site_url, 'site_depend': site_info.site_depend}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelSite(request):
    if request.method == "POST":
        site_id = request.POST.get("site_id")
        models.Site.objects.get(id=site_id).delete()
        return HttpResponse("已删除")


@login_required
@Perms_required
def Depend(request):
    title = '环境部署'

    hostgroup_obj = HostGroup.objects.all()
    tree_info = []
    n = 1
    for i in hostgroup_obj:
        hostgroup_id = i.id
        hostgroup_name = i.group_name
        hostinfo_obj = HostInfo.objects.filter(host_group_id=hostgroup_id)
        if n == 1:
            tree_info.append({"id": hostgroup_id, "pId": 0,
                              "name": hostgroup_name, "open": "true"})
        else:
            tree_info.append({"id": hostgroup_id, "pId": 0,
                              "name": hostgroup_name, "open": "false"})
        n += 1
        for j in hostinfo_obj:
            host_id = j.id
            host_ip = j.IP
            id = hostgroup_id * 10 + host_id
            if j.os_type == "Linux":
                tree_info.append(
                    {"id": id, "pId": hostgroup_id, "name": host_ip})
            else:
                pass
    data = json.dumps(tree_info, ensure_ascii=False)

    depend_obj = models.Depend.objects.all()
    depend_list = []
    for depend in depend_obj:
        depend_id = depend.id
        depend_name = depend.depend_name
        depend_version = depend.depend_version

        install_script = depend.install_script
        depend_list.append({'depend_id': depend_id, 'depend_name': depend_name,
                            'depend_version': depend_version, 'install_script': install_script})
    return render(request, "code_depend.html", locals())


@csrf_exempt
@login_required
@Perms_required
def AddDepend(request):
    if request.method == 'POST':
        depend_name = request.POST.get('depend_name')
        depend_version = request.POST.get('depend_version')

        install_script = request.POST.get('install_script')

        try:
            depend_obj = models.Depend(
                depend_name=depend_name, depend_version=depend_version, install_script=install_script)
            depend_obj.save()
            return HttpResponse('添加成功')
        except:
            return HttpResponse('添加失败')
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def EditDepend(request):
    if request.method == "POST":
        depend_id = request.POST.get("depend_id")
        depend_name = request.POST.get('depend_name')
        depend_version = request.POST.get('depend_version')

        install_script = request.POST.get('install_script')
        action = request.POST.get("action", None)
        if action:
            depend_obj = models.Depend.objects.get(id=depend_id)
            depend_obj.depend_name = depend_name
            depend_obj.depend_version = depend_version

            depend_obj.install_script = install_script
            depend_obj.save()
            return HttpResponse("修改成功")
        else:
            depend_info = models.Depend.objects.get(id=depend_id)
            info_json = {'depend_id': depend_info.id, 'depend_name': depend_info.depend_name,
                         'depend_version': depend_info.depend_version, 'install_script': depend_info.install_script}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelDepend(request):
    if request.method == "POST":
        depend_id = request.POST.get("depend_id")
        models.Depend.objects.get(id=depend_id).delete()
        return HttpResponse("已删除")


@csrf_exempt
@login_required
@Perms_required
def Install(request):

    if request.method == "POST":
        depend_id = request.POST.get("depend_id")
        ip_json = request.POST.get("node_id_json")

        ip_list = []
        for i in json.loads(ip_json):
            if re.search("\d+.\d+.\d+.\d", i):
                ip_list.append(i)
        depend_obj = models.Depend.objects.get(id=depend_id)
        install_script = depend_obj.install_script
        depend_name = depend_obj.depend_name

        script_name = "install_%s" % depend_name

        script_file = os.path.join(BASE_DIR, 'static', 'scripts', script_name)

        f = open(script_file, 'wb')

        f.write(install_script)

        f.close()

        script_file = "salt://%s" % script_file

        result = salt_script.Install(ip_list, script_file)

        return HttpResponse(result)


@login_required
@Perms_required
def PostCode(request, page_id=1):

    title = '站点发布'

    ip_obj = HostInfo.objects.filter(
        Q(host_group_id=3) | Q(host_group_id=2) | Q(host_group_id=1))

    ip_list = []
    for i in ip_obj:
        ip_list.append(i.IP)

    site_info = models.Site.objects.all()
    site_list = []

    for site in site_info:
        site_name = site.site_name
        site_list.append({"site_name": site_name, 'site_id': site.id})

    project_info = models.Project.objects.all()
    project_list = []

    for project in project_info:
        project_name = project.project_name
        project_list.append(
            {'project_name': project_name, 'project_id': project.id})

    post_list = []
    post_obj = models.CodePost.objects.all().order_by('post_ip')

    p = Paginator(post_obj, 13)
    current_page = p.page(page_id)

    for i in current_page:
        site_info = models.Site.objects.get(id=i.post_site_id)
        site_name = site_info.site_name
        site_project = site_info.project

        info = {'ip': i.post_ip, 'site_name': site_name, 'site_project': site_project, 'site_msg': i.postsite_msg, 'site_path': i.site_path,
                'current_version': i.current_version, 'version_info': i.version_info, 'upcode_date': i.upcode_date, 'post_id': i.id, 'author': i.author}
        post_list.append(info)

    return render(request, "code_post.html", locals())


@csrf_exempt
@login_required
@Perms_required
def AddPost(request):
    if request.method == 'POST':
        site_name = request.POST.get('site_name')
        post_ip = request.POST.get('post_ip')
        site_dir = request.POST.get('site_dir')
        postsite_msg = request.POST.get('postsite_msg')
        post_ip = json.loads(post_ip)
        site_url = models.Site.objects.filter(site_name=site_name)[0].site_url

        post_site_id = models.Site.objects.get(site_name=site_name).id

        for ip in post_ip:
            code_obj = models.CodePost(
                post_site_id=post_site_id, post_ip=ip, site_path=site_dir, postsite_msg=postsite_msg)
            code_obj.save()
            cmd = "salt '%s' cmd.script salt:///opt/scripts/syncode.py" % ip
        try:
            pass
            return HttpResponse('发布成功')
        except:
            return HttpResponse('发布失败')
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def UpCode(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')

        post_obj = models.CodePost.objects.get(id=post_id)

        site_name = models.Site.objects.get(id=post_obj.post_site_id)
        ip = post_obj.post_ip

        site_path = post_obj.site_path

        cmd = "salt '%s' cmd.run 'cd %s/%s && git stash && git pull  origin master'   runas='www'" % (
            ip, site_path, site_name)

        cmdform = '-1  --pretty=format:"%H-%an-%ad-%s"'

        cmd_version = "salt '%s' cmd.run 'cd %s/%s && git log %s'" % (
            ip, site_path, site_name, cmdform)

        status, output = os.popen(cmd)

        if status == 0:
            logmsg = os.popen(cmd_version)
            log_info = logmsg.split("\n")[1].strip().split('-')
            current_version = log_info[0]
            version_info = log_info[3]
            author = log_info[1]
            upcode_date = log_info[2]

            str_date = upcode_date.strip('+0800').strip()

            array_date = time.strptime(str_date, "%a %b %d %H:%M:%S %Y")

            upcode_date = time.strftime('%Y-%m-%d %H:%M:%S', array_date)

            if current_version == post_obj.current_version:
                msg = "+++++++++已经是最新版本+++++++\n"
            else:
                # 同步版本信息
                post_obj.current_version = current_version
                post_obj.version_info = version_info
                post_obj.author = author
                post_obj.upcode_date = upcode_date
                post_obj.save()

                msg = "+++++++++++更新成功++++++++++\n" + output

                # 添加更新记录
                try:
                    record_obj = models.PostRecord(
                        current_version=current_version, version_info=version_info, author=author, upcode_date=upcode_date, CodePost_id=post_id)
                    record_obj.save()

                except:
                    pass

        else:
            msg = "+++++++++++更新失败++++++++++\n" + output

        return HttpResponse(msg)

    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelPost(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        models.CodePost.objects.get(id=post_id).delete()
        record_obj = models.PostRecord.objects.filter(CodePost_id=post_id)
        for record in record_obj:
            record.delete()
        return HttpResponse("已删除")


@csrf_exempt
@login_required
@Perms_required
def FilterSite(request):
    if request.method == 'POST':
        site_id = request.POST.get('site_id')
        project_id = request.POST.get('project_id')
        ip = request.POST.get('ip')
        if site_id:
            if site_id == '0':
                post_obj = models.CodePost.objects.all()
            else:
                post_obj = models.CodePost.objects.filter(post_site_id=site_id)

        elif project_id:
            if project_id == '0':
                post_obj = models.CodePost.objects.all()
            else:
                project_obj = models.Project.objects.get(id=project_id)
                site_obj = models.Site.objects.filter(
                    project_id=project_obj.id)

                # 合并多个查询
                post_obj = models.CodePost.objects.none()
                for site in site_obj:
                    post_obj = post_obj | models.CodePost.objects.filter(
                        post_site_id=site.id)

        elif ip:
            if ip == '0':
                post_obj = models.CodePost.objects.all()
            else:
                post_obj = models.CodePost.objects.filter(post_ip=ip)

        else:
            pass

        post_list = []
        for i in post_obj:
            site_info = models.Site.objects.get(id=i.post_site_id)
            site_name = site_info.site_name
            site_project = site_info.project

            info = {'ip': i.post_ip, 'site_name': site_name, 'site_project': site_project, 'site_msg': i.postsite_msg,
                    'site_path': i.site_path, 'current_version': i.current_version, 'version_info': i.version_info,
                    'upcode_date': i.upcode_date, 'post_id': i.id, 'author': i.author}
            post_list.append(info)

        return render(request, "code_codepost_table.html", locals())


@login_required
@Perms_required
def RecordLog(request, post_id):

    title = '站点发布'

    record_info = models.PostRecord.objects.filter(
        CodePost_id=post_id).order_by('-upcode_date')

    post_obj = models.CodePost.objects.get(id=post_id)

    current_version = post_obj.current_version

    record_list = []

    for i in record_info:
        upcode_date = i.upcode_date
        site_name = i.CodePost.post_site
        post_ip = i.CodePost.post_ip

        if i.current_version == current_version:
            version_status = u"当前版本"
        else:
            version_status = u"历史版本"

        record_list.append({'record_id': i.id, 'site_name': site_name, 'post_ip': post_ip, 'current_version': i.current_version,
                            'version_info': i.version_info, 'author': i.author, 'upcode_date': upcode_date, 'version_status': version_status})

    return render(request, "code_record.html", locals())


@csrf_exempt
@login_required
@Perms_required
def RollBack(request):
    if request.method == 'POST':
        record_id = request.POST.get('record_id')

        record_obj = models.PostRecord.objects.get(id=record_id)

        rollback_version = record_obj.current_version

        post_id = record_obj.CodePost_id

        post_obj = models.CodePost.objects.get(id=post_id)

        site_name = models.Site.objects.get(id=post_obj.post_site_id)

        ip = post_obj.post_ip

        site_path = post_obj.site_path

        cmd = "salt '%s' cmd.run 'cd %s/%s && git reset %s'   runas='www'" % (
            ip, site_path, site_name, rollback_version)

        status, output = os.popen(cmd)

        if status == 0:

            current_version = record_obj.current_version
            version_info = record_obj.version_info
            author = record_obj.author
            upcode_date = record_obj.upcode_date

            # 同步版本信息
            post_obj.current_version = current_version
            post_obj.version_info = version_info
            post_obj.author = author
            post_obj.upcode_date = upcode_date

            post_obj.save()

            msg = "+++++++++++回滚成功++++++++++\n" + output

        else:
            msg = "+++++++++++回滚失败++++++++++\n" + output

        return HttpResponse(msg)

    else:
        return HttpResponse("未知请求")
