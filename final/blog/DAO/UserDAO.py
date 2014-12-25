# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()

from blog.models import User


# basic operation
def new_user(**user):
    result = User.objects.create(**user)
    return result


def delete_user(user_id):
    User.objects.get(id=user_id).delete()


def get_user_by_id(user_id):
    return User.objects.get(id=user_id)


def get_user_by_phone(user_phone):
    return User.objects.get(phone=user_phone)


def update_user(**kw):
    User.objects.filter(id=kw['id']).update(**kw)

