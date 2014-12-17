# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

import datetime

# django import
from blog.DAO import AddFriendDAO
from blog.DAO import FriendDAO
from blog.DAO import MessageDAO

from blog.models import Addfriend
from blog.models import Message

from django.db import IntegrityError
from django.db import transaction

'''
添加好友请求Service, 主要实现, 添加好友时发送请求, 记录入数据库, 成功添加后删除记录.
'''


# user send an addfriend request
def addfriend(user_id, receiver_id):

    # object create
    new_friend = {"userid": user_id, "friendid": receiver_id, "datetime": datetime.datetime.now()}
    addfriend_request = Addfriend.object.create(new_friend)
    message = {"userid": receiver_id, "type": "3", "content": user_id + " wants to add you"}
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


# user confirm his friend
def confirm_addfriend(userid, friendid, addfriend_id, type):

    # type = 1 represents agree to add
    if type == "1":
        friend = {"userid": userid, "friendid": friendid}
        message = {"userid": friendid, "type": "4", "content": userid + " agree to add you"}
        try:
            with transaction.atomic():
                result = FriendDAO.new_friend(**friend)
                AddFriendDAO.delete_addfriend(addfriend_id)
                MessageDAO.new_message(**message)

        except IntegrityError:
            result = "error"

        return result

    # type = 2 represents refuse to add
    else:
        message = {"userid": friendid, "type": "4", "content": userid + " refuse to add you"}
        try:
            with transaction.atomic():
                AddFriendDAO.delete_addfriend(addfriend_id)
                MessageDAO.new_message(**message)

        except IntegrityError:
            result = "error"

        return result





