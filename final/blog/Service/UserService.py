__author__ = 'Joeeee'

# python modules
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

# django modules
import django
django.setup()

# my app's modules
from blog.DAO import UserDAO
from blog.DAO import BlogDAO
from django.db import Error
from blog.Utils import GenerateObject


def register_user(**new_user):
    try:
        u = UserDAO.new_user(**new_user)
        return u
    except Error:
        return "error"
    # u = UserDAO.new_user(**new_user)

# register_user(phone="xuanlang", password="zhuzhu", sex="female", nickname="zhuzhu")


def search_user(phone):

    try:
        user = UserDAO.get_user_by_phone(phone)
    except:
        return None

    # fix data, pop useless data
    u = GenerateObject.todcit(user)
    u.pop("last_longitude")
    u.pop("last_latitude")
    u.pop("head")
    u.pop("password")

    # get userid
    userid = user.id

    try:
        blog = BlogDAO.get_blog_by_userid(userid)

        # if this user has no blog
        if len(blog) == 0:
            return u
    except:
        return u

    # return the latest blog
    result_blog = []
    for i in range(0, len(blog)):
        result_blog.append(blog[i])

    result_blog.sort(lambda x, y: cmp(x.datetime, y.datetime))

    # change result_blog into dict type and remove userid attr, 'cause user already have it
    r = GenerateObject.todcit(result_blog[0])

    # pop useless data
    r.pop("userid")
    r.pop("photoid")

    # fix latitude and longitude decimal problem
    r['longitude'] = str(r['longitude'])
    r['latitude'] = str(r['latitude'])

    final_result = {"user": u, "blog": r}
    return final_result


def delete_user(user_id):
    try:
        UserDAO.delete_user(user_id)
    except Error:
        return "error"
    return 'success'


def get_user_by_id(user_id):
    try:
        u = UserDAO.get_user_by_id(user_id)
    except Error:
        u = None
    return u


def update_user_info(user):
    try:
        UserDAO.update_user(**user)
    except Error:
        return "error"
    return "success"


def validate_user_by_phone(phone, password):
    try:
        user = UserDAO.get_user_by_phone(phone)
    except:
        return "error"

    if user.password == password:
        return user
    else:
        return "error"
