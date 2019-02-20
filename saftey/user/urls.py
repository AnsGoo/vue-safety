"""saftey URL Configuration

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
from user import views
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('register/', views.register, name='register'),
    path(r'login/', obtain_jwt_token),
    # path('login/', views.login, name='login'),
    path('user/get_user/', views.get_user),
    path('user/profile/add/', views.profile_add),
    path('user/profile/update/<int:id>/',
         views.profile_update, name='profile_update'),
    path('user/pwdchange/<int:id>/', views.pwd_change),
    path('logout/', views.logout, name='logout'),
    path('forget_password/', views.logout, name='logout'),
    path('vaild_email/', views.vaild_email),
    path('vaild_username/', views.vaild_username),
    path('user/profile/edit/', views.profile_edit),
    path('user/get_department/', views.get_department),
    path('user/profile/show/', views.profile_show),
    path('user/get_cities/', views.get_cities),
    path('user/get_areas/', views.get_areas),
    path('user/profile/info/', views.get_user_info),
]
