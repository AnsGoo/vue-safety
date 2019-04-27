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
from app_code import views

urlpatterns = [
    url('^project/$', views.Project),
    url('^editproject/$', views.EditProject),
    url('^delproject/$', views.DelProject),
    url('^addproject/$', views.AddProject),


    url('^site/$', views.Site),
    url('^editsite/$', views.EditSite),
    url('^addsite/$', views.AddSite),
    url('^delsite/$', views.DelSite),

    url('^postcode/page_id=(\d+)/$', views.PostCode),
    url('^postcode/$', views.PostCode),
    url('^filtersite/$', views.FilterSite),
    url('^addpost/$', views.AddPost),
    url('^upcode/$', views.UpCode),
    url('^rollback/$', views.RollBack),
    url('^delpost/$', views.DelPost),
    url('^recordlog/post_id=(\d+)/$', views.RecordLog),


    url('^depend/$', views.Depend),
    url('^editdepend/$', views.EditDepend),
    url('^deldepend/$', views.DelDepend),
    url('^addepend/$', views.AddDepend),
    url('^install/$', views.Install),
]
