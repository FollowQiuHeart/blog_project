#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django.conf.urls import url

__author__ = "qiu"
__date__ = "2019-11-04 19:45"

from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('index/', Index.as_view(), name='index'),  # 首页
    path('about/', About.as_view(), name='about'),  # 关于
    path('archive/', Archive.as_view(), name='archive'),  # 归档
    path('link/', Link.as_view(), name='link'),   # 链接
    path('message', Message.as_view(), name='message'),   # 留言
    path('article/<int:pk>/', Articles.as_view(), name='article'),   # 文章列表
    path('get_comment/', GetComment, name='get_comment'),  # 留言信息回推接收
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),   # 文章详情
    path('search/', Search.as_view(), name='search'),     # 全局搜索处理
    path('tag/<int:id>/', Tagcloud.as_view(), name='tag'),   # 标签云
    path('login/',Login.as_view(),name='login'), #登录界面
    path('register/', Register.as_view(), name='register'),  # 登录界面
    # url("^login$",views.login_view,name="login_view"),
    url('^check_status/$', views.check_status, name='check_status'), #检测状态
    url('^send_sms_codes/$',views.send_sms_codes,name="send_sms_codes") #发送验证码
]