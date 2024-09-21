"""
URL configuration for Django_Next project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

import Project01.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', Project01.views.index, name='index'),
    path('tocourse/', Project01.views.to_course),
    path('book/list', Project01.views.bookList),
    path('book/list2', Project01.views.bookList2),
    path('book/preAdd', Project01.views.preAdd),
    path('book/preAdd2', Project01.views.preAdd2),
    path('book/preAdd3', Project01.views.preAdd3),
    path('book/add', Project01.views.add),
    path('book/preUpdate/<int:id>', Project01.views.preUpdate),
    path('book/update', Project01.views.update),
    path('book/delete/<int:id>', Project01.views.delete),
    path('transfer', Project01.views.transfer),
    # 跳转注册
    path('toRegister/', Project01.views.to_register, name='toRegister'),
    # 提交注册请求
    path('auth/register', Project01.views.register),
    # 跳转登录
    path('tologin/', Project01.views.to_login),
    # 提交登录请求
    path('auth/login', Project01.views.login),
    # 修改密码 get请求直接跳转页面,post请求执行事务处理
    path('auth/setPwd', Project01.views.setPwd),
    # 跳转主页
    path('auth/index', Project01.views.to_index),
    # 用户注销
    path('auth/logout', Project01.views.logout),

]
