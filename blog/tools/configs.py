# -*- encoding: utf-8 -*-
"""
@File    : configs.py
@Time    : 3/24/20 9:50 AM
@Author  : qiuyucheng
@Software: PyCharm
"""
import time
import jwt
TOKEN_KEY = "1234567ab"
CODE_TOKEN_KEY="qiu1234567"

# 生成token
def make_token(username, exp, now_datetime):
    key = '1234567ab'
    now_t = time.time()
    payload = {"username": username, "login_time": str(now_datetime), "exp": int(now_t + exp)}
    return jwt.encode(payload, key, algorithm="HS256")
