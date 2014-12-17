__author__ = 'assiso'
# -*- coding: utf-8 -*-

####################################################
#
#   除了  UserVerify(request) 这个函数为了调用的方便返回值为True 或 False
#   其余全部字符串，如  UserRegister(UserCode,Password)  返回值为"Register Success""Register False"
#
#   切记，除了检测用户是否登陆、用户登陆、用户登出传入的参数为 request 外，其余全是 UserCode + Password
#
#
####################################################
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")




from django.contrib.auth.models import User
from django.contrib import auth


# 用户注册
# Joe
def UserRegister(usercode, password):
    try:
        user = User.objects.create_user(username=usercode, email='NULL', password=password)
        user.is_staff = True
        return True
    except:
        return False
# boolean = UserRegister("zhuzhu","zhurun")
# print boolean

#管理员注册
def AdminRegister(self):
    return "Success"


#用户登陆
def UserLogin(request, usercode, password):
    user = auth.authenticate(username=usercode, password=password)
    if user is not None:
        auth.login(request, user)
        return True
    else:
        return False

#用户登出
def UserLogoff(request):
    auth.logout(request)
    return "Logoff Success"

#检测用户是否登陆
def UserVerify(request):
    if request.user.is_authenticated():
        return True
    else:
        return False

#用户更改密码
def UserChangePassWord(UserCode,Password):
    user = User.objects.get(username=UserCode)
    if user is None:
        return "no such person"
    else:
        user.set_password(Password)
        user.save()
        return "Change Success"
