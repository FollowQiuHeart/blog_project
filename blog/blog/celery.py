# -*- encoding: utf-8 -*-
"""
@File    : celery.py
@Time    : 3/22/20 8:47 PM
@Author  : qiuyucheng
@Software: PyCharm
"""
from celery import Celery
from django.conf import settings
import os

# 为celery设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

# 创建celery应用/实例,名称为sms_codes

app = Celery('sms_codes',
             backend='redis://:@127.0.0.1:6379/1', #redis存储
             broker='redis://:@127.0.0.1:6379/2')
# #配置好celery的backend和broker
# app = Celery("sms_codes")
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# 配置应用
# app.conf.update(
#     # 配置broker
#     BACKEND_URL='redis://:@127.0.0.1:6379/1',
#     BROKER_URL='redis://:@127.0.0.1:6379/2',
# )
# 设置app自动加载任务
app.autodiscover_tasks(settings.INSTALLED_APPS)