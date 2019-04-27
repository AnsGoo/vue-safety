# coding:utf-8


import json

from django.shortcuts import render, HttpResponse

from app_rbac import models

from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from app_auth.views import Perms_required


@csrf_exempt
@login_required
@Perms_required
def UserMg(request):

    roles = models.Role.objects.all()
    role_list = []
    for role in roles:
        role_list.append({"role_title": role.role_title, "role_id": role.id})

    user_info = models.UserInfo.objects.all()
    user_list = []

    for user in user_info:

        role = models.Role.objects.filter(id=user.role_id)
        user_list.append({"name": user.user.last_name, "user_id": user.user.id, "username": user.user.username,
                          'phone': user.phone, 'email': user.user.email, 'role': role[0].role_title, 'status': user.status})

    return render(request, "rbac_usermg.html", {'title': '用户管理', 'role_info': role_list, 'user_info': user_list})


@csrf_exempt
@login_required
@Perms_required
def AddUser(request):
    if request.method == "POST":
        name = request.POST.get("name")
        username = request.POST.get("username")
        passwd = request.POST.get("passwd")
        role = request.POST.get("role")
        phone = request.POST.get("phone")
        email = request.POST.get("email")

        try:
            # django自带用户信息表
            user_obj = User.objects.create_user(
                username=username, email=email, password=passwd, last_name=name)
            user_obj.save()

            # 保存用户信息
            # 用户信息拓展表
            user_obj = models.UserInfo(
                user=user_obj, role_id=role, phone=phone)
            user_obj.save()

            return HttpResponse("用户添加成功")
        except:
            return HttpResponse("用户名已被注册!")
    else:
        return render(request, "rbac_usermg.html", {'title': '用户管理'})


@csrf_exempt
@login_required
@Perms_required
def EditUser(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        name = request.POST.get("name")
        username = request.POST.get("username")
        role = request.POST.get("role")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        action = request.POST.get("action", None)

        if action:

            user_obj = User.objects.get(id=user_id)
            user_obj.last_name = name
            user_obj.username = username
            user_obj.email = email
            user_obj.save()

            userinfo_obj = models.UserInfo.objects.get(user_id=user_id)
            userinfo_obj.role_id = role
            userinfo_obj.phone = phone

            userinfo_obj.save()
            return HttpResponse("修改成功")
        else:

            user_info = User.objects.get(id=user_id)

            user_eobj = models.UserInfo.objects.get(user=user_info)
            info_json = {'user_id': user_info.id, 'name': user_info.last_name, 'username': user_info.username,
                         'role': user_eobj.role_id, 'phone': user_eobj.phone, 'email': user_info.email}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelUser(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user_obj = User.objects.get(id=user_id)
        models.UserInfo.objects.get(user=user_obj).delete()
        user_obj.delete()
        return HttpResponse("已删除")


@csrf_exempt
@login_required
@Perms_required
def Role(request):
    title = '角色管理'

    role_info = models.Role.objects.all()
    role_list = []
    for role in role_info:
        role_list.append({"role_title": role.role_title,
                          "role_msg": role.role_msg, 'role_id': role.id})
    return render(request, "rbac_role.html", locals())


@csrf_exempt
@login_required
@Perms_required
def AddRole(request):
    if request.method == "POST":
        role_title = request.POST.get("role_title")
        role_msg = request.POST.get("role_msg")
        try:
            role_obj = models.Role(role_title=role_title, role_msg=role_msg)
            role_obj.save()
            return HttpResponse("添加成功")
        except:
            return HttpResponse("角色已存在!")
    else:
        return render(request, "rbac_role.html", {'title': 'ht'})


@csrf_exempt
@login_required
@Perms_required
def EditRole(request):
    if request.method == "POST":
        role_id = request.POST.get("role_id")
        role_title = request.POST.get("role_title")
        role_msg = request.POST.get("role_msg")
        action = request.POST.get("action", None)
        if action:
            role_obj = models.Role.objects.get(id=role_id)
            role_obj.role_title = role_title
            role_obj.role_msg = role_msg
            role_obj.save()
            return HttpResponse("修改成功")
        else:
            role_info = models.Role.objects.get(id=role_id)
            info_json = {'role_id': role_info.id,
                         'role_title': role_info.role_title, 'role_msg': role_info.role_msg}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelRole(request):
    if request.method == "POST":
        role_id = request.POST.get("role_id")
        models.Role.objects.get(id=role_id).delete()
        return HttpResponse("已删除")


@csrf_exempt
@login_required
@Perms_required
def RolePerms(request):
    if request.method == "POST":
        role_id = request.POST.get("role_id")

        # 获取会话用户角色
        role_obj = models.Role.objects.get(id=role_id)

        # 获取用户拥有的权限
        perms_list = role_obj.perms.all()

        perms_num_list = []
        for i in perms_list:
            perms_num_list.append(i.perms_num)

        perms_obj = models.Permission.objects.all()

        nodes = []

        # 创建分页对象

        for perms in perms_obj:
            if perms.perms_num in perms_num_list:

                nodes.append({"id": perms.perms_num, "pId": perms.pmenu_id,
                              "name": perms.perms_title, 'open': True, 'checked': True})
            else:
                nodes.append({"id": perms.perms_num, "pId": perms.pmenu_id,
                              "name": perms.perms_title, 'open': True})

        ztr_data = json.dumps(nodes)

        return HttpResponse(ztr_data)


#
@csrf_exempt
@login_required
@Perms_required
def AddRolePerms(request):
    if request.method == "POST":
        perms_nums = request.POST.get("node_id_json")
        role_id = request.POST.get("role_id")

        role_obj = models.Role.objects.get(id=role_id)

        perms_nums = json.loads(perms_nums)
        perms_ids = []
        for i in perms_nums:
            perms_obj = models.Permission.objects.get(perms_num=i)
            perms_ids.append(perms_obj.id)
        role_obj.perms.set(perms_ids)

        return HttpResponse('权限已更新')
    else:
        return HttpResponse("未知请求")


@login_required
@Perms_required
def Permission(request, page_id=1):
    title = u'权限管理'
    perms_obj = models.Permission.objects.all()
    perms_list = []

    for perms in perms_obj:
        perms_dict = {}
        perms_dict['perms_title'] = perms.perms_title

        perms_dict['perms_id'] = perms.perms_num
        perms_dict['pmenu_id'] = perms.pmenu_id

        perms_list.append(perms_dict)

    perms_obj = models.Permission.objects.all().order_by('perms_num')

    nodes = []
    node_dict = {}

    # 创建分页对象
    p = Paginator(perms_obj, 14)

    # 当前页
    current_page = p.page(page_id)

    for perms in current_page:

        node_id = perms.perms_num

        node_dict[node_id] = {"perms_id": perms.id, "perms_title": perms.perms_title, "perms_url": perms.perms_url,
                              "perms_type": perms.perms_type, "perms_icon": perms.perms_icon, "perms_num": perms.perms_num, "pmenu_id": perms.pmenu_id}

        nodes.append(node_id)

    perms_info = []

    nodes = sorted(nodes)

    for node_id in nodes:
        perms_info.append(node_dict[node_id])

    return render(request, "rbac_permission.html", locals())


#
@csrf_exempt
@login_required
@Perms_required
def AddPermission(request):
    if request.method == "POST":
        perms_title = request.POST.get("perms_title")
        perms_url = request.POST.get("perms_url")
        perms_type = request.POST.get("perms_type")
        pmenu_id = request.POST.get("pmenu_id")
        perms_icon = request.POST.get("perms_icon")

        if perms_type == u"一级菜单":
            pmenu_id = 0
        else:
            pass

        try:
            perms_obj = models.Permission(perms_title=perms_title, perms_url=perms_url,
                                          perms_type=perms_type, pmenu_id=pmenu_id, perms_icon=perms_icon)
            perms_obj.save()

            if perms_obj.perms_type == u"一级菜单":
                perms_num = perms_obj.id
            else:
                perms_num = int(str(pmenu_id)+'0'+str(perms_obj.id))

            perms_obj.perms_num = perms_num
            perms_obj.save()
            return HttpResponse("权限已添加")
        except:
            return HttpResponse("权限名称或地址已存在")

    else:
        return render(request, "rbac_permission.html", {'title': '权限管理'})


@csrf_exempt
@login_required
@Perms_required
def EditPerms(request):
    if request.method == "POST":
        perms_id = request.POST.get("perms_id")
        perms_title = request.POST.get("perms_title")
        perms_url = request.POST.get("perms_url")
        perms_type = request.POST.get("perms_type")
        pmenu_id = request.POST.get("pmenu_id")
        perms_icon = request.POST.get("perms_icon")

        action = request.POST.get("action", None)
        if action:

            if perms_type == u"一级菜单":
                pmenu_id = 0
            else:
                pass

            perms_obj = models.Permission.objects.get(id=perms_id)
            perms_obj.perms_title = perms_title
            perms_obj.perms_url = perms_url
            perms_obj.perms_type = perms_type
            perms_obj.pmenu_id = pmenu_id

            perms_obj.perms_icon = perms_icon

            perms_obj.save()

            if perms_type == u"一级菜单":
                perms_num = perms_id
            else:
                perms_num = int(str(pmenu_id)+'0'+str(perms_id))

            perms_obj.perms_num = perms_num
            perms_obj.save()

            return HttpResponse("修改成功")
        else:
            perms_info = models.Permission.objects.get(id=perms_id)

            print(perms_id)
            info_json = {'perms_id': perms_info.id, 'perms_title': perms_info.perms_title, 'perms_url': perms_info.perms_url,
                         'perms_type': perms_info.perms_type, 'pmenu_id': perms_info.pmenu_id, 'perms_icon': perms_info.perms_icon}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelPerms(request):
    if request.method == "POST":
        perms_id = request.POST.get("perms_id")
        models.Permission.objects.get(id=perms_id).delete()
        return HttpResponse("已删除")


# 修改用户密码
@csrf_exempt
@login_required
@Perms_required
def change_passwd(request):
    if request.method == 'POST':
        new_passwd = request.POST.get("new_passwd")
        user_id = request.POST.get("user_id")

        user_obj = User.objects.get(id=user_id)

        user_obj.set_password(new_passwd)
        user_obj.save()

        msg = "密码已修改"

        return HttpResponse(msg)
    else:
        return HttpResponse("未知请求")
