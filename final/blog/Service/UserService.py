__author__ = 'Joeeee'

# python modules
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

# django modules
import django
django.setup()

# my app's modules
from blog.DAO import UserDAO


def register_user(**new_user):
    try:
        u = UserDAO.new_user(**new_user)
        return u
    except:
        return "error"
    # u = UserDAO.new_user(**new_user)

# register_user(phone="xuanlang", password="zhuzhu", sex="female", nickname="zhuzhu")


def delete_user(user_id):
    try:
        UserDAO.delete_user(user_id)
    except:
        return "error"
    return 'success'


def get_user_by_id(user_id):
    try:
        u = UserDAO.get_user_by_id(user_id)
    except:
        u = None
    return u


def update_user_info(user):
    try:
        UserDAO.update_user(**user)
    except:
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


def sign_in(phone, password):
    pass