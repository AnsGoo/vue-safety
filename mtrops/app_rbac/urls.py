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
from app_rbac import views

urlpatterns = [
    path('usermg/', views.UserMg),
    path('adduser/', views.AddUser),
    path('edituser/', views.EditUser),
    path('deluser/', views.DelUser),
    url('^perms/page_id=(\d+)/$', views.Permission),
    path('perms/', views.Permission),
    path('addperms/', views.AddPermission),
    path('editperms/', views.EditPerms),
    path('delperms/', views.DelPerms),

    path('role/', views.Role),
    path('addrole/', views.AddRole),
    path('editrole/', views.EditRole),
    path('delrole/', views.DelRole),
    path('roleperms/', views.RolePerms),
    path('addroleperms/', views.AddRolePerms),
    #url('^menu/page_id=(\d+)/$', views.Menu),
    path('chpasswd/', views.change_passwd),
]
