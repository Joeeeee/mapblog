# -*- coding: utf-8 -*-

__author__ = 'Joeeee'

# Modules in my app
from blog.Service import AddFriendService
from blog.Service import BlogService
from auth import Httpsession
from blog.Service import UserService
from blog.Utils import GenerateObject
# from blog.models import User


# Modules in Django
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django import forms

# Module in Python
import json


'''
Create your views here.
'''


# for test
@csrf_exempt
def helloworld(request):
    return render(request, "RealMapBlog/login.html")


#user register
@csrf_exempt
def register(request):

    if request.method == 'POST':
        # print request
        # get data
        phone = request.POST['phone']
        password = request.POST['password']
        sex = request.POST['sex']
        nickname = request.POST['nickname']

        if Httpsession.UserRegister(phone, password):
            result = UserService.register_user(phone=phone, sex=sex, nickname=nickname)

            if result != "error":
                # return render_to_response("RealMapBlog/login.html", {"success": "1"})
                return HttpResponse(json.dumps({"success": "1"}))
            else:
                return HttpResponse(json.dumps({"success": "0", "type": "1"}))

        else:
            return HttpResponse(json.dumps({"success": "0", "type": "0"}))


@csrf_exempt
def login(request):

    if request.method == 'POST':

        # get data
        phone = request.POST['phone']
        password = request.POST['password']

        if Httpsession.UserLogin(request, phone, password):
            # return render_to_response("RealMapBlog/index.html", {"success": "1"})
            return HttpResponse(json.dumps({"success": "1"}))

        else:
            # return render_to_response("RealMapBlog/login.html", {"success": "0"})
            return HttpResponse(json.dumps({"success": "0"}))


# send an add friend request
@csrf_exempt
def add_friend(request):

    if Httpsession.UserVerify(request):
        # suppose POST method
        # get data
        user_id = request.POST['userid']
        receiver_id = request.POST['friendid']

        result = AddFriendService.addfriend(user_id, receiver_id)

        # only one kind of error, that is database error
        if result == "fail":
            return HttpResponse(json.dumps({"success": "0", "type": "0"}))

        else:
            return HttpResponse(json.dumps({"success": "1"}))
    else:
        # haven't been signed in
        return HttpResponse(json.dumps({"success": "0", "type": "1"}))


@csrf_exempt
def confirm_add_friend(request):

    if Httpsession.UserVerify(request):

        # get data
        user_id = request.POST['userid']
        friend_id = request.POST['friendid']
        add_friend_id = request.POST['addfriendid']
        confirm_type = request.POST['type']

        result = AddFriendService.confirm_addfriend(user_id, friend_id, add_friend_id, confirm_type)

        if result == "error":
            return HttpResponse(json.dumps({"success": "0"}))

        else:
            # get friend's detail
            friend = GenerateObject.todcit(UserService.get_user_by_id(friend_id))
            return HttpResponse(json.dumps({"success": "1", "friend": friend}))



@csrf_exempt
def publish_blog(request):

    if request.method == 'POST':

        if Httpsession.UserVerify(request):

            # get data
            content = request.POST['content']
            longitude = float(request.POST['longitude'])
            latitude = float(request.POST['latitude'])
            userid = request.POST['userid']

            result = BlogService.newblog(userid, longitude, latitude, content)

            if result is None:
                return HttpResponse(json.dumps({"success": "0", "type": "0"}))

            else:
                return HttpResponse(json.dumps(GenerateObject.todcit(result)))


@csrf_exempt
def logoff(request):
    pass


@csrf_exempt
def search_friend(request):
    pass


@csrf_exempt
def get_friend_blog(request):
    pass


@csrf_exempt
def get_add_friend_detail(request):
    pass


@csrf_exempt
def delete_blog(request):
    pass


@csrf_exempt
def delete_comment(request):
    pass

@csrf_exempt
def delete_friend(request):
    pass


@csrf_exempt
def edit_info(request):
    pass


@csrf_exempt
def comment(request):
    pass


@csrf_exempt
def refresh_friend_blog(request):
    pass


@csrf_exempt
def setup_group(request):
    pass


@csrf_exempt
def add_groupmember(request):
    pass


@csrf_exempt
def delete_groupmember(request):
    pass


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

# print GenerateObject.todcit(UserService.get_user_by_id(13))