from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
import json
from DAO import UserDAO
from DAO import BlogDAO
from blog.models import Blog
from blog.models import User

from auth.Httpsession import*

# Create your views here.


def helloworld(request):
    return render(request, 'adam2014/helloworld.html')


def new_blog(request):
    if request.method == 'POST':
        user_id = request['user_id']
        content = request['content']
        latitude = request['latitude']
        longitude = request['longitude']
        time = request['time']
        blog = {'content': content, 'latitude': latitude, 'longitude': longitude, 'userid': user_id, 'time': time}
        BlogDAO.insert_blog(**blog)


def register(request):
    if request.method == 'POST':
        username = request['username']
        userid = request['userid']
        password = request['password']
        try:
            user = User.objects.get(userid=userid)
        except ObjectDoesNotExist:
            pass
        if user != None:
            return render_to_response("register.html", {'msg': {"用户已存在"}})
        user = {'userid': userid, 'username': username, 'password': password}
        UserDAO.add_user(user)


