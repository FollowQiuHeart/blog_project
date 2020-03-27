#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "qiu"
__date__ = "2019-07-03 16:47"

# 常规模块的引入分为三部分，依次为：
# Python内置模块（如json、datetime）、第三方模块（如Django）、自己写的模块

from datetime import datetime  # 内置的日期时间模块

from django.db import models  # 创建Django模型
from django.contrib.auth.models import AbstractUser  # Django自带的用户模块


# 继承Django自带的用户管理模块，在后台可以创建多个用户，并可设置用户权限
class User(AbstractUser):
    """用户信息"""
    phone = models.CharField(verbose_name="手机号",max_length=11)
    login_time = models.DateTimeField(verbose_name="登录时间",null=True)

    class Meta:  # 元类，可定义该模块的基本信息
        verbose_name = '用户数据'
        verbose_name_plural = verbose_name

    def __str__(self):  # 当print输出实例对象，或str() 实例对象时，调用这个方法
        return self.username


class Category(models.Model):
    """博客分类"""
    name = models.CharField(verbose_name='文档分类', max_length=20)
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)  # datetime.now不可加()，这样在创建实例时调用该方法
    edit_time = models.DateTimeField(verbose_name='修改时间', default=datetime.now)

    class Meta:
        verbose_name = '文档分类'
        verbose_name_plural = verbose_name #复数名称也为文档分类

    def __str__(self): #输出类实例时,会调用__str__,我们将该方法重写,用于美化输出
        return self.name


class Tagprofile(models.Model):
    """标签管理"""
    tag_name = models.CharField('标签名', max_length=30)

    class Meta:
        verbose_name = '标签名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


class Blog(models.Model):
    """博客文章"""
    title = models.CharField(verbose_name='博客文章', max_length=50, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, verbose_name='文章分类')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='作者')
    content = models.TextField(verbose_name='内容')
    digest = models.TextField(verbose_name='摘要', default='')
    add_time = models.DateTimeField(verbose_name='创建时间', default=datetime.now)
    edit_time = models.DateTimeField(verbose_name='更新时间', default=datetime.now)
    read_nums = models.IntegerField(verbose_name='阅读数', default=0)
    conment_nums = models.IntegerField(verbose_name='评论数', default=0)
    image = models.ImageField(verbose_name='博客封面', upload_to='blog/%Y/%m')
    tag = models.ManyToManyField(Tagprofile)

    def viewed(self):
        """
        增加阅读数
        """
        self.read_nums += 1
        self.save(update_fields=['read_nums'])

    def commenced(self):
        """
        增加评论数
        """
        self.conment_nums += 1
        self.save(update_fields=['conment_nums'])

    class Meta:
        verbose_name = '博客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Conment(models.Model):
    """对博客评论"""
    user = models.CharField(verbose_name='评论用户', max_length=25)
    title = models.CharField(verbose_name="标题", max_length=100)
    source_id = models.CharField(verbose_name='文章id或source名称', max_length=25)
    conment = models.TextField(verbose_name='评论内容')
    add_time = models.DateTimeField(verbose_name='添加时间', default=datetime.now)
    url = models.CharField(verbose_name='链接', max_length=100)

    class Meta:
        verbose_name = '评论信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Message(models.Model):
    """留言"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='用户')
    message = models.TextField(verbose_name='留言')
    add_time = models.DateTimeField(verbose_name='时间', default=datetime.now)

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message
