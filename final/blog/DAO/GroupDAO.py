# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()

from blog.models import Group


# basic operation
def new_group(**group):
    result = Group.object.create(**group)
    return result


def delete_group(group_id):
    Group.object.get(id=group_id).delete()


def get_group_by_id(group_id):
    result = Group.object.get(id=group_id)
    return result


def update_group(**group):
    Group.objects.filter(id=group['id']).update(**group)