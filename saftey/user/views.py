# -*- coding: utf-8 -*-
import json
import logging
import datetime

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


from .models import AuthUser
from CompanySafteyManage.models import Company
from CompanySafteyManage.models import Department
from utils.DataUtils import MySQLUtils
from utils.DateUtils import ComplexEncoder
from .models import Profile
from .models import Eduction
from .models import Workhistory
from .models import Cities
from .models import Provinces
from .models import Areas
log = logging.getLogger('scripts')


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get('new_username')
        password = request.POST.get('new_password')
        email = request.POST.get('new_email')
        user = User.objects.create_user(
            username=username, password=password, email=email)
        return HttpResponseRedirect("/login/")

@csrf_exempt
def get_user(request):
    user = request.user
    print(user)
    status=False
    login_user = None
    if user=='AnonymousUser':
        status = True
        login_user={'userame':user.userame}
    return HttpResponse(json.dumps({'status':status,'user':login_user}))

@csrf_exempt
def login(request):
    '''
    function: 登陆操作
    return:
    autor: 成海文
    create_date: 2018-12-1
    '''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        log.info(user.username)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponse(json.dumps({'user':username}))
            # return HttpResponseRedirect('/company/index')
        else:
            # return render(request, 'login.html', {'msg': 'user or password is not exist'})
            return HttpResponse(json.dumps({'user': None}))
    return render(request, 'login.html', {'msg': None})


@csrf_exempt
def vaild_email(request):
    email = request.POST.get('email')
    if email is not None:
        user_set = User.objects.filter(email__exact=email)
        if len(user_set) == 0:
            return HttpResponse(json.dumps({'status': 'usable'}))
        else:
            return HttpResponse(json.dumps({'status': 'disable'}))
    else:
        return HttpResponse(json.dumps({'status': None}))


@csrf_exempt
def vaild_username(request):
    username = request.POST.get('username')
    if username is not None:
        user_set = User.objects.filter(username__exact=username)
        if len(user_set) == 0:
            return HttpResponse(json.dumps({'status': 'usable'}))
        else:
            return HttpResponse(json.dumps({'status': 'disable'}))
    else:
        return HttpResponse(json.dumps({'status': None}))


def profile_update(request, id):
    pass
    return HttpResponse(request, json.dumps({'status': 'OK'}))

@csrf_exempt
def profile_add(request):
    global  log
    user =request.user
    if user:
        log.info(user)
        firstname= request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        idcard = request.POST.get('IDCard')
        telephone = request.POST.get('telephone')
        qq = request.POST.get('qq')
        content = request.POST.get('content')
        wechat = request.POST.get('wechat')
        eduction = request.POST.get('eduction')
        school = request.POST.get('school')
        major = request.POST.get('major')
        institute = request.POST.get('institute')
        startdate  = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        # company = request.POST.get('company')
        department_id = request.POST.get('department')
        print('department:%s'%department_id)
        department = Department.objects.get(id=int(department_id))
        employeedate = request.POST.get('joindate')
        jobs = request.POST.get('jobs')
        address = request.POST.get('address')
        user.first_name = firstname
        user.last_name = lastname
        user.is_active = 1
        birthdate = idcard[6:10]+'-'+idcard[10:12]+'-'+idcard[12:14]
        sex='unkonw'
        if  department :
            user.is_staff = 1
        user.save()
        if idcard and int(idcard[16])%2==1:
            sex='male'
        elif idcard and int(idcard[16])%2==0:
            sex ='female'
        profile = Profile.objects.filter(user =user)
        if profile:
            profile.update(user=user,telephone =telephone,wechat=wechat,qq=qq,department=department,idcard = idcard,jobs=jobs,sex=sex,description=content,address=address,employeedate=employeedate,birthdate=birthdate)
        else:
            profile = Profile(user=user,telephone =telephone,wechat=wechat,qq=qq,department=department,idcard = idcard,jobs=jobs,sex=sex,description=content,address=address,employeedate=employeedate,birthdate=birthdate)
            profile.save()
        eduction_set  = Eduction.objects.filter(name=eduction).filter(user=user)
        if len(eduction_set)>0:
            eduction_set.update(school=school,institute=institute,major=major,startdate=startdate,enddate=enddate)
        else:
            eduction = Eduction(user=user,name=eduction,school=school,institute=institute,major=major,startdate=startdate,enddate=enddate)
            eduction.save()     
        return HttpResponseRedirect(r'/user/profile/show')
    else:
        return HttpResponseRedirect(r'/login/')


def pwd_change(request, id):
    pass
    return HttpResponse(request, json.dumps({'status': 'OK'}))


def logout(request):
    auth.logout(request)
    # return HttpResponseRedirect("login")
    return HttpResponse('OK')

@login_required(login_url='/login/')
def profile_edit(request):
    company_set = Company.objects.all()
    province_set = Provinces.objects.all()
    # print(province_set)
    # print(len(province_set))
    return render(request, r'person\edit.html', {'companys': company_set,'province_set':province_set })


@csrf_exempt
def get_department(request):
    company_id = request.POST.get('id')
    global log
    log.info(company_id)
    sql = 'select id,name as text,type from department where company_id = '
    dbutil = MySQLUtils()
    result = dbutil.get_dict_data(sql + company_id)
    for line in result:
        department_id = line['id']
        raw = rescursive_departments(str(department_id))
        if len(raw) > 0:
            line["children"] = raw
    return HttpResponse(json.dumps(result))


def rescursive_departments(id):
    sql = 'select id,name as text,type from department where fatherdepartment = '
    dbutil = MySQLUtils()
    result = dbutil.get_dict_data(sql + id)
    if len(result) > 0:
        for line in result:
            child_result = dbutil.get_dict_data(sql + str(line['id']))
            if len(child_result) > 0:
                line["children"] = child_result
    return result

def profile_show(request):
    global  log
    user =request.user
    if user:
        return render(request,r'person/show.html')
    else:
        return HttpResponseRedirect(r'/login/')

@login_required(login_url='/login/')
@csrf_exempt
def get_user_info(request):
    user = request.user
    profile = Profile.objects.filter(user=user)[0]
    eduction_set = Eduction.objects.filter(user=user)
    workhistory_set = Workhistory.objects.filter(user=user)
    brithdate = profile.idcard[6:14]
    age = datetime.datetime.now().year - int(brithdate[:4])
    user_info = {'telephone':profile.telephone,'age':age,'sex':profile.sex,'brithdate':profile.birthdate,'address':profile.address,'description':profile.description,'qq':profile.qq,'wechat':profile.wechat}
    department = profile.department
    company = department.company
    company_info = {'cid':company.id,'company':company.name,'did':department.id,'department':department.name,'description':company.description,'address':company.address,'logo':company.logo}
    eduction_list = [{'id':ed.id,'name':ed.name,'school':ed.school,'institute':ed.institute,'major':ed.major,'startdate':ed.startdate,'enddate':ed.enddate} for ed in eduction_set]
    workhistory_list = [{'id':w.id,'company':w.company,'project':w.project,'department':w.department,'jobs':w.jobs,'startdate':w.startdate,'enddate':w.enddate} for w in workhistory_set]
    return HttpResponse(json.dumps({'profile':user_info,'eductions':eduction_list,'workhistorys':workhistory_list,'company':company_info},cls = ComplexEncoder))

@csrf_exempt
def get_cities(request):
    id = request.POST.get('id')
    # province = Provinces.objects.get(id=int(id))
    city_set = Cities.objects.filter(province__id=int(id))
    cities =[{'id': city.id,'name':city.name}  for city in city_set]
    return HttpResponse(json.dumps({'cities':cities}))

@csrf_exempt
def get_areas(request):
    id = request.POST.get('id')
    # province = Provinces.objects.get(id=int(id))
    area_set = Areas.objects.filter(city__id=int(id))
    areas =[{'id': area.id,'name':area.name}  for area in area_set]
    return HttpResponse(json.dumps({'areas':areas}))


