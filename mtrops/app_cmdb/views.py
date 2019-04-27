#coding:utf-8

import json
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app_cmdb import models
from app_cmdb import sysinfo
from app_cmdb import exp_cmdb
from app_rbac.models import UserInfo
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from app_auth.views import Perms_required
from django.contrib.auth.models import User
from app_cmdb.tasks import SyncHost_job
from mtrops import settings




@login_required
@Perms_required
def Idc(request):
    idc_info = models.IDC.objects.all()
    idc_list = []


    for idc in idc_info:
        idc_list.append({"idc_name":idc.idc_name,"msg":idc.msg,'idc_id':idc.id})

    return render(request,"cmdb_idc.html",{'title':'IDC','idc_list':idc_list})


@csrf_exempt
@login_required
@Perms_required
def AddIdc(request):
    if request.method == "POST":
        idc_name = request.POST.get("idc_name")
        idc_msg = request.POST.get("idc_msg")
        try:
            idc_obj = models.IDC(idc_name=idc_name,msg=idc_msg)
            idc_obj.save()
            return HttpResponse("添加成功")
        except:
            return HttpResponse("IDC已存在!")
    else:
        return HttpResponse("未知请求")



@csrf_exempt
@login_required
@Perms_required
def EditIdc(request):
    if request.method == "POST":
        idc_name = request.POST.get("idc_name")
        idc_msg = request.POST.get("idc_msg")
        idc_id = request.POST.get("idc_id")
        action = request.POST.get("action", None)
        if action:
            idc_obj = models.IDC.objects.get(id=idc_id)
            idc_obj.idc_name=idc_name
            idc_obj.msg = idc_msg
            idc_obj.save()
            return HttpResponse("修改成功")
        else:
            idc_info = models.IDC.objects.get(id=idc_id)
            info_json = {'idc_id':idc_info.id,'idc_name':idc_info.idc_name,'idc_msg':idc_info.msg}
            info_json = json.dumps(info_json)

            return HttpResponse(info_json)

    else:
        return HttpResponse("未知请求")




@csrf_exempt
@login_required
@Perms_required
def DelIdc(request):
    if request.method == "POST":
        idc_id = request.POST.get("idc_id")

        models.IDC.objects.get(id=idc_id).delete()

        return HttpResponse("已删除")



#主机组页面
@login_required
@Perms_required
def HostGroup(request):
    group_info = models.HostGroup.objects.all()
    group_list = []
    for group in group_info:
        group_list.append({"group_name":group.group_name,"msg":group.msg,'id':group.id})
    return render(request,"cmdb_group.html",{'title':'主机组','group_list':group_list})



@csrf_exempt
@login_required
@Perms_required
def AddGroup(request):
    if request.method == "POST":
        group_name = request.POST.get("group_name")
        group_msg = request.POST.get("group_msg")
        try:
            group_obj = models.HostGroup(group_name=group_name,msg=group_msg)
            group_obj.save()
            return HttpResponse("添加成功")
        except:
            return HttpResponse("主机组已存在")
    else:
        return HttpResponse("未知请求")



@csrf_exempt
@login_required
@Perms_required
def EditGroup(request):

    if request.method == "POST":
        group_name = request.POST.get("group_name")
        group_msg = request.POST.get("group_msg")
        group_id = request.POST.get("group_id")
        action = request.POST.get("action", None)
        if action:
            group_obj = models.HostGroup.objects.get(id=group_id)
            group_obj.group_name=group_name
            group_obj.msg = group_msg
            group_obj.save()
            return HttpResponse("修改成功")
        else:
            group_info = models.HostGroup.objects.get(id=group_id)
            info_json = {'group_id':group_info.id,'group_name':group_info.group_name,'group_msg':group_info.msg}
            info_json = json.dumps(info_json)

            return HttpResponse(info_json)

    else:
        return HttpResponse("未知请求")



@csrf_exempt
@login_required
@Perms_required
def DelGroup(request):
    if request.method == "POST":
        group_id = request.POST.get("group_id")

        models.HostGroup.objects.get(id=group_id).delete()

        return HttpResponse("已删除")




@login_required
@Perms_required
def HostInfo(request,page_id=1):

    title = 'CMDB'

    host_info = models.HostInfo.objects.all().order_by('id')

    idc_list = []
    group_list = []
    host_list = []
    remote_user_list = []

    idc_info = models.IDC.objects.all()
    group_info = models.HostGroup.objects.all()
    remote_user_info = models.LoginUser.objects.all()

    # 创建分页对象
    p = Paginator(host_info, 14)
    #当前页
    current_page = p.page(page_id)


    for idc in idc_info:
        idc_list.append({'idc_id':idc.id,'idc_name':idc.idc_name})

    for group in group_info:
        group_list.append({'group_id':group.id,'group_name':group.group_name})

    for login_user in remote_user_info:
        remote_user_list.append({'login_user_id':login_user.id,'login_user_name':login_user.login_user})


    for host in current_page:
        host_group = models.HostGroup.objects.filter(id=host.host_group_id)[0].group_name
        idc = models.IDC.objects.filter(id=host.idc_id)[0].idc_name

        host_list.append({'host_id':host.id,'hostname':host.hostname,'IP':host.IP,'host_group':host_group,
                          'device_type':host.device_type,'status':host.status,'idc':idc,'msg':host.msg})

    return render(request, "cmdb_host.html", locals())


@login_required
@Perms_required
def Detailinfo(request,ip):

    title = 'CMDB'

    host_info = models.HostInfo.objects.get(IP=ip)

    return render(request, "cmdb_host_info.html", locals())



@csrf_exempt
@login_required
@Perms_required
def FilterHost(request):
    if request.method == "POST":

        host_list = []

        idc_id = request.POST.get('idc_id',0)
        host_group_id = request.POST.get('hostgroup_id', 0)
        device_type = request.POST.get('device_type', u'设备类型')
        info_search = request.POST.get('info_search', None)

        idc_id = int(idc_id)

        host_group_id = int(host_group_id)

        if idc_id==0 and host_group_id==0 and device_type == u'设备类型':

            if info_search:
                host_info = models.HostInfo.objects.filter(Q(IP__icontains=info_search) | Q(hostname__icontains=info_search) | Q(msg__icontains=info_search) | Q(in_ip__icontains=info_search))

            else:
                host_info = models.HostInfo.objects.all().order_by('id')
        else:

            if idc_id!=0 and host_group_id == 0 and  device_type == u'设备类型':
                host_info = models.HostInfo.objects.filter(idc_id=idc_id).order_by('id')


            elif idc_id==0 and host_group_id != 0 and  device_type == u'设备类型':

                host_info = models.HostInfo.objects.filter(host_group_id=host_group_id).order_by('id')



            elif idc_id==0 and host_group_id == 0 and  device_type != u'设备类型':
                host_info = models.HostInfo.objects.filter(device_type=device_type).order_by('id')


            elif idc_id!=0 and host_group_id != 0 and  device_type == u'设备类型':
                host_info = models.HostInfo.objects.filter(Q(idc_id=idc_id) & Q(host_group_id=host_group_id))

            elif idc_id==0 and host_group_id != 0 and  device_type != u'设备类型':
                host_info = models.HostInfo.objects.filter(Q(device_type=device_type) & Q(host_group_id=host_group_id))

            elif idc_id!=0 and host_group_id == 0 and  device_type != u'设备类型':
                host_info = models.HostInfo.objects.filter(Q(device_type=device_type) & Q(idc_id=idc_id))
            else:
                host_info = models.HostInfo.objects.filter(Q(device_type=device_type) & Q(idc_id=idc_id) & Q(host_group_id=host_group_id))




        for host in host_info:
            host_group = models.HostGroup.objects.filter(id=host.host_group_id)[0].group_name
            idc = models.IDC.objects.filter(id=host.idc_id)[0].idc_name

            host_list.append({'hostname': host.hostname, 'IP': host.IP, 'host_group': host_group,
                              'device_type': host.device_type, 'status': host.status, 'idc': idc, 'msg': host.msg})


    return render(request, "cmdb_host_table.html", locals())




@csrf_exempt
@login_required
@Perms_required
def AddHost(request):
    if request.method == "POST":
        IP = request.POST.get("IP")
        username = int(request.POST.get("username"))
        device_type = request.POST.get("device_type")
        idc = request.POST.get("idc")
        port = request.POST.get("port")
        host_group = request.POST.get("host_group")
        msg = request.POST.get("msg")

        try:
            host_obj = models.HostInfo(IP=IP, remote_user_id=username,  device_type=device_type, idc_id=idc,
                                       port=port, host_group_id=host_group, msg=msg)
            host_obj.save()
            return HttpResponse("设备已添加")
        except:
            return HttpResponse("添加失败")

    else:
        return HttpResponse("未知请求")




@csrf_exempt
@login_required
@Perms_required
def SyncHost(request):
    if request.method == "POST":
        ips = request.POST.get("ips")

        if ips == 'all':
            ips = []
            host_objs =  models.HostInfo.objects.all()
            for ip in host_objs:
                ips.append(ip.IP)
            
        else:
            ips = ips.strip(',').split(',')


        data = sysinfo.main(ips)
        for ip in data.keys():
            host_obj = models.HostInfo.objects.get(IP=ip)
            sys_info = data[ip]
            host_obj.hostname = sys_info['localhost']
           #host_obj.in_ip = sys_info['']
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

        return  HttpResponse('已同步')

        #任务队列
        # if len(ips) <= 3:
        #     pass
        # else:
        #     r = SyncHost_job.delay(ips)
        #     result =  r.get()
        #     return  HttpResponse('任务正在执行中：%s' % r)
    else:
        return HttpResponse("未知请求")


@csrf_exempt
@login_required
@Perms_required
def DelHost(request):
    if request.method == "POST":
        ips = request.POST.get("ips")

        ips = ips.strip(',').split(',')

        for ip in ips:
            models.HostInfo.objects.get(IP=ip).delete()

        return HttpResponse("已删除")




@csrf_exempt
@login_required
@Perms_required
def EditHost(request):
    if request.method == "POST":
        action = request.POST.get("action",None)
        if action:
            host_id = request.POST.get("host_id")
            IP = request.POST.get("IP")
            username = request.POST.get("username")
            device_type = request.POST.get("device_type")
            idc = request.POST.get("idc")
            port = request.POST.get("port")
            host_group = request.POST.get("host_group")
            msg = request.POST.get("msg")

            edit_host_info = models.HostInfo.objects.get(id=host_id)
            edit_host_info.IP=IP
            edit_host_info.remote_user_id=int(username)
            edit_host_info.device_type=device_type
            edit_host_info.idc_id=idc
            edit_host_info.port=port
            edit_host_info.host_group_id=host_group
            edit_host_info.msg=msg

            edit_host_info.save()

            return HttpResponse("信息已修改")

        else:
            ip = request.POST.get("ip")
            edit_host_info = models.HostInfo.objects.get(IP=ip)

            info_json = {'host_id':edit_host_info.id,'ip':edit_host_info.IP,'username':edit_host_info.remote_user_id,'device_type':edit_host_info.device_type,'idc':edit_host_info.idc_id,'port':edit_host_info.port,'host_group':edit_host_info.host_group_id,'msg':edit_host_info.msg}
            info_json = json.dumps(info_json)
            return HttpResponse(info_json)





@csrf_exempt
@login_required
@Perms_required
def ExpCmdb(request):
    if request.method == "POST":
        ips = request.POST.get("ips")
        if ips == 'all':
            sql = "select a.IP,a.hostname,b.idc_name,a.device_type,c.group_name,a.service_type,d.login_user,d.login_passwd," \
                  "a.msg,a.port,a.os_type,a.kernel,a.os_version,a.mem_total,a.mem_swap,a.cpu_type,a.cpu_num,a.mount_home ," \
                  "a.mount_root,a.mount_alidata,a.status from app_cmdb_hostinfo a,app_cmdb_idc b,app_cmdb_hostgroup c,app_cmdb_loginuser d"\
                  " where a.idc_id=b.id and a.host_group_id=c.id and a.remote_user_id=d.id;"

            exp_cmdb.main(sql)
            return HttpResponse('http://%s:8080/static/media/cmdb.xlsx' % settings.HOST)
        else:
            return HttpResponse('http://%s:8080/static/media/cmdb.xlsx' % settings.HOST)




@csrf_exempt
@login_required
@Perms_required
def LoginUser(request):
    title = '系统账号'

    user_obj = UserInfo.objects.all()

    user_list = []
    for i in user_obj:
        user_id = i.id
        username = i.user.last_name

        user_list.append({"user_id":user_id,'username':username})


    info_obj = models.LoginUser.objects.all()

    login_user_list = []

    for i in info_obj:
        if i.private_key:
            private_key = i.private_key
        else:
            private_key = "None"
        login_user_list.append({"login_user_id":i.id,"login_user": i.login_user, "last_name": i.people.user.last_name,'phone':i.people.phone,'email':i.people.user.email,'private_key':private_key})



    return render(request,"cmdb_loginuser.html",locals())



@csrf_exempt
#@login_required
#@Perms_required
def AddLoginUser(request):
    if request.method == "POST":

        login_user = request.POST.get("login_user")

        login_passwd = request.POST.get("login_passwd")

        login_key = request.POST.get("login_key")

        people = request.POST.get("people")

        try:
            login_user_obj = models.LoginUser(login_user=login_user,login_passwd=login_passwd,private_key=login_key,people_id=people)
            login_user_obj.save()
            return HttpResponse("添加成功")
        except:
            return HttpResponse("用户已存在!")
    else:
        return HttpResponse("未知请求")



@csrf_exempt
#@login_required
#@Perms_required
def EditLoginUser(request):
    if request.method == "POST":
        login_user_id = request.POST.get("login_user_id")

        login_user = request.POST.get("login_user")

        login_passwd = request.POST.get("login_passwd")

        login_key = request.POST.get("login_key")

        people = request.POST.get("people")

        action = request.POST.get("action", None)
        if action:
            login_user_obj = models.LoginUser.objects.get(id=login_user_id)
            login_user_obj.login_user=login_user
            login_user_obj.login_passwd = login_passwd
            login_user_obj.private_key = login_key
            login_user_obj.people_id = people

            login_user_obj.save()
            return HttpResponse("修改成功")
        else:
            login_user_info = models.LoginUser.objects.get(id=login_user_id)
            info_json = {'login_user_id':login_user_info.id,"login_user":login_user_info.login_user,"login_passwd":login_user_info.login_passwd,"private_key":login_user_info.private_key,"people":login_user_info.people_id}
            info_json = json.dumps(info_json)

            return HttpResponse(info_json)

    else:
        return HttpResponse("未知请求")




@csrf_exempt
#@login_required
#@Perms_required
def DelLoginUser(request):
    if request.method == "POST":
        login_user_id = request.POST.get("login_user_id")
        models.LoginUser.objects.get(id=login_user_id).delete()
        return HttpResponse("已删除")

