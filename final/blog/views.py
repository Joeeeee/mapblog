# -*- coding: utf-8 -*-

__author__ = 'Joeeee'

# Modules in my app
from blog.Service import AddFriendService
from auth import Httpsession
from blog.models import User


# Modules in Django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django import forms

# Module in Python
import json

'''
实现简单的博客功能
功能: 1、用户注册; 2、用户发博客; 3、用户查看自己发的博客;
'''

# Create your views here.


# for test
@csrf_exempt
def helloworld(request):
    return render(request, "RealMapBlog/login.html")


# send an add friend request
@csrf_exempt
def addfriend(request):

    if Httpsession.UserVerify(request):
        # suppose POST method
        # get data
        user_id = request.POST['user_id']
        receiver_id = request.POST['receiver_id']

        result = AddFriendService.addfriend(user_id, receiver_id)

        # only one kind of error, that is database error
        if result == "fail":
            return HttpResponse(json.dumps({"success": "0", "type": "0"}))
        else:
            return HttpResponse(json.dumps({"success": "1"}))
    else:
        # haven't been signed in
        return HttpResponse(json.dumps({"success": "0", "type": "1"}))


# class UserForm(forms.Form):
#     headImg = forms.FileField()
#
# @csrf_exempt
# def testfile(request):
#     if request.method == "POST":
#         uf = UserForm(request.POST, request.FILES)
#         if uf.is_valid():
#             #获取表单信息
#             headImg = uf.cleaned_data['headImg']
#             print headImg
#             #写入数据库
#             user = User()
#             user.nickname = "Joe"
#             user.age = "1"
#             user.city = "Foshan"
#             user.password = "12345678"
#             user.info = "111"
#             user.phone = "18688282803"
#             user.head = headImg
#             user.save()
#             return HttpResponse('upload ok!')
#     else:
#         pass
#     return HttpResponse("success")