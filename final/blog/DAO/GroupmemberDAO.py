# -*- coding: utf-8 -*-
__author__ = 'Joeeee'


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()

from blog.models import Groupmember


# basic operation
def new_groupmember(**groupmember):
    result = Groupmember.object.create(**groupmember)
    return result


def delete_groupmember_by_id(groupmember_id):
    Groupmember.object.get(id=groupmember_id).delete()


def get_groupmember_by_id(groupmember_id):
    result = Groupmember.object.get(id=groupmember_id)
    return result


def update_groupmember(**groupmember):
    Groupmember.objects.filter(id=groupmember['id']).update(**groupmember)