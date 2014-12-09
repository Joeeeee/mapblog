# -*- coding: utf-8 -*-
__author__ = 'Joeeeeee'


# Modules in my app
from blog.Service import UserService
from blog.Service import BlogService
from auth.Httpsession import*


# Modules in Django
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def register(request):
    if request.method == 'GET':
        phone = request.GET['phone']

        # 验证用户手机号

        if True:
            return HttpResponse(json.dumps({"success": 1}))
        if False:
            return HttpResponse(json.dumps({"success": 0}))

    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        username = request.POST['nickname']

        # 插入数据库

        if True:
            return HttpResponse(json.dumps({"success": 1}))
        if False:
            return HttpResponse(json.dumps({"success": 0}))

@csrf_exempt
def sign_in(request):

    # phone = request.POST['phone']
    # password = request.POST['password']
    #
    # user = UserService.validate_user_by_phone(phone, password)
    #
    # if user == "error":
    #     return HttpResponse(json.dumps({"result": 0}))
    #
    # else:
    #     return HttpResponse("success")

    return render(request, "RealMapBlog/index.html")