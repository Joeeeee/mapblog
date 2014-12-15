# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

import os
os.environ.setdefault("DJANGO_SETTING_MODULE", "final.settings")

from blog.models import Friend


# basic operation
def new_friend(**friend):
    result = Friend.object.create(**friend)
    return result


def delete_friend(friend_id):
    Friend.object.get(id=friend_id).delete()


def get_friend_by_id(friend_id):
    result = Friend.object.get(id=friend_id)
    return result


def update_friend(**friend):
    Friend.objects.filter(id=friend['id']).update(**friend)