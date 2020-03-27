#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "qiu"
__date__ = "2020-12-05 19:48"

from django.contrib import admin
from .models import Blog, Conment, Category, Tagprofile, Message


class BlogAdmin(admin.ModelAdmin):
    list_filter = ['title', 'category', 'author']
    list_display = ['title', 'category', 'author', 'add_time']
    pass


class ConmentAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogAdmin)
admin.site.register(Conment, ConmentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tagprofile, TagAdmin)
admin.site.register(Message, MessageAdmin)
