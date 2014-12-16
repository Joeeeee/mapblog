# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

import datetime

# django import
from blog.DAO import AddFriendDAO
from blog.DAO import MessageDAO
from blog.models import Addfriend
from blog.models import Message
from django.db import IntegrityError
from django.db import transaction

'''
添加好友请求Service, 主要实现, 添加好友时发送请求, 记录入数据库, 成功添加后删除记录.
'''


def addfriend(user_id, receiver_id):

    # object create
    new_friend = {"userid": user_id, "friendid": receiver_id, "datetime": datetime.datetime.now()}
    addfriend_request = Addfriend.object.create(new_friend)
    message = {"userid": receiver_id, "type": "1", "content": user_id + " wants to add you"}
    addfriend_message = Message.objects.create(message)

    # object commit
    try:
        with transaction.atomic():
            result = AddFriendDAO.new_addfriend(**addfriend_request)

            # add receiver's message
            MessageDAO.new_message(**addfriend_message)

    except IntegrityError:
        result = "fail"

    return result

