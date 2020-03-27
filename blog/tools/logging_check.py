# -*- encoding: utf-8 -*-
"""
@File    : logging_check.py
@Time    : 3/19/20 6:28 PM
@Author  : qiuyucheng
@Software: PyCharm
"""
import jwt
from myblog.models import User
from django.http import JsonResponse
from tools.configs import TOKEN_KEY

def logging_check(*methods):
    def _logging_check(func):
        def wrapper(request,*args,**kwargs):
            #逻辑判断
            #1.判断当前请求是否需要校验
            #2.取出token
            #3.如果需要校验token,如何校验
            if not methods:
                return func(request,*args,**kwargs)
            else:
                if request.method not in methods:
                    return func(request, *args, **kwargs)
            #取出token
            token = request.META.get("HTTP_AUTHORIZATION")
            if not token:
                result = {"code":20104,'error':'Please login'}
                return JsonResponse(result)
            try:
                res = jwt.decode(token,TOKEN_KEY,algorithms="HS256")
            except Exception as e:
                result = {"code":20105,"error":"Please login"}
                return JsonResponse(result)

            username = res["username"]
            #取出token里的login_time
            login_time = res["login_time"]
            print("-----------------------------------------")
            print(login_time)
            print(type(login_time))

            user = User.objects.get(username=username)
            print(user.login_time)
            print(type(user.login_time))
            print("------------------------------------------")
            if login_time:
                if str(user.login_time) != login_time:
                    result = {"code":20106,"error":"Other people have logined!please"
                                                   "login again!!"}
                    return JsonResponse(result)
            request.user = user
            return func(request,*args,**kwargs)
        return wrapper
    return _logging_check

def get_user_by_request(request):
    #尝试获取用户身份
    #return user or None
    token = request.META.get("HTTP_AUTHORIZATION")
    if not token:
        #用户没有登录
        return None
    try:
        res = jwt.decode(token,TOKEN_KEY,algorithms="HS256")
    except Exception as e:
        return None

    username = res['username']
    users = User.objects.filter(username=username)
    if not users:
        return None
    return users[0]