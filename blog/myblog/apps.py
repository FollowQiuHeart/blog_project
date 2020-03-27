# _*_ coding:utf-8 _*_
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'myblog'
    verbose_name = '博客信息'   # 定义后台管理界面，中文显示应用名称
