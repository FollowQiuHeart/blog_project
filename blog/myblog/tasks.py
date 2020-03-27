# -*- encoding: utf-8 -*-
"""
@File    : tasks.py
@Time    : 3/22/20 8:59 PM
@Author  : qiuyucheng
@Software: PyCharm
"""
import json
import logging

import jwt
from tools.configs import CODE_TOKEN_KEY
from blog.celery import app
import time
from tools import zhenzismsclient as smsclient
import random
import hashlib
from django.http import JsonResponse


@app.task(name="send_sms_code")
def send_sms_code(mobile):
    """
        发送短信验证码
        :param mobile: 手机号
        :param sms_num: 验证码
        :param expires: 有效期
        :return: None
    """
    # 生成四位数的随机验证码
    print("手机号为：", mobile)
    code = ''
    for num in range(1, 5):
        code = code + str(random.randint(0, 9))
    print("随机验证码为：", code)
    # 将AppId和AppSecret复制粘贴过来
    client = smsclient.ZhenziSmsClient('https://sms_developer.zhenzikj.com', "104954",
                                       "5ed8bef8-45b9-41f4-a012-85631d6aa5d9")
    # 第一个参数为发送号码，第二个参数为发送的验证码内容
    payload = {"code":code,"exp":time.time()+60} #要进行加密的数据
    code_token = jwt.encode(payload=payload,key=CODE_TOKEN_KEY,algorithm="HS256")
    print("code_token", code_token)
    try:
        result = client.send({
                "message": '您的验证码为' + code + "，感谢您观看本博客!!",
                "number": mobile})
        # 注意result为str类型，并不是字典
        result = json.loads(result)  #将json字符串转为json格式
        if result.get("code") == 0:
            result = {
                "code":200,
                "data":{
                    "info":result.get("data"),
                    "code_token":code_token.decode()}} #将字节串转为字符串
            print("result.data:",result)
        else:
            result = {
                "code":result.get("code"),
                "error":result.get("data")
            }
            print("result.error:",result)
    except Exception as e:
        result = {"code": 10101, "error": "发送失败"}
        print("发送短信验证码失败！手机号：%s" % mobile)
    return result
