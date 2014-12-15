# -*- coding: utf-8 -*-

__author__ = 'Joeeee'

# Modules in my app
from blog.Service import AddFriendService
from auth import Httpsession


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