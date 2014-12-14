__author__ = 'Joeeee'

# -*- coding: utf-8 -*-

from blog.models import User

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


# basic operation
def new_user(**user):
    result = User.object.create(**user)
    return result


def delete_user(user_id):
    User.objects.get(id=user_id).delete()


def get_user_by_id(user_id):
    return User.objects.get(id=user_id)


def get_user_by_phone(user_phone):
    return User.objects.get(userid=user_phone)


def update_user(**kw):
    User.objects.filter(id=kw['id']).update(**kw)

