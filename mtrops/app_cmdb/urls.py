from django.conf.urls import url, include
from app_sys import views
"""mtrops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from app_cmdb import views

urlpatterns = [
    path('hostinfo/<int:id>', views.HostInfo),
    path('hostinfo/', views.HostInfo),
    path('addhost/', views.AddHost),
    path('delhost/', views.DelHost),
    path('synchost/', views.SyncHost),
    url('^detailinfo/ip=(\d+.\d+.\d+.\d+)/$', views.Detailinfo),
    path('filterhost/', views.FilterHost),
    path('expcmdb/', views.ExpCmdb),
    path('edithost/', views.EditHost),
    path('loginuser/', views.LoginUser),
    path('addlguser/', views.AddLoginUser),
    path('dellguser/', views.DelLoginUser),
    path('editlguser/', views.EditLoginUser),

    path('idc/', views.Idc),
    path('editidc/', views.EditIdc),
    path('delidc/', views.DelIdc),
    path('addidc/', views.AddIdc),

    path('hostgroup/', views.HostGroup),
    path('addgroup/', views.AddGroup),
    path('editgroup/', views.EditGroup),
    path('delgroup/', views.DelGroup),
]
