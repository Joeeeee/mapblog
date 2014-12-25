# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

import datetime

# django import
from blog.DAO import AddFriendDAO
from blog.DAO import FriendDAO
from blog.DAO import MessageDAO
from blog.DAO import UserDAO

from django.db import IntegrityError
from django.db import transaction

'''
添加好友请求Service, 主要实现, 添加好友时发送请求, 记录入数据库, 成功添加后删除记录.
'''


# user send an addfriend request
def addfriend(user_id, receiver_id):

    try:
        with transaction.atomic():
            # get user
            u = UserDAO.get_user_by_id(user_id)
            r = UserDAO.get_user_by_id(receiver_id)
    except:
        return "fail"

    # object create
    new_friend = {"userid": u, "friendid": receiver_id, "datetime": datetime.datetime.now()}
    # addfriend_request = Addfriend.object.create(new_friend)
    message = {"userid": r, "type": "3", "content": u.nickname + " wants to add you"}
    # addfriend_message = Message.objects.create(message)

    # object commit
    try:
        with transaction.atomic():
            result = AddFriendDAO.new_addfriend(**new_friend)

            # add receiver's message
            MessageDAO.new_message(**message)

    except IntegrityError:
        result = "fail"

    return result


# user confirm his friend
def confirm_addfriend(userid, friendid, addfriend_id, confirm_type):

    try:
        with transaction.atomic():
            # get user
            u = UserDAO.get_user_by_id(userid)
            f = UserDAO.get_user_by_id(friendid)
    except:
        return "fail"

    # type = 1 represents agree to add
    if confirm_type == "1":

        # construct record
        friend_user = {"userid": u, "friendid": friendid}
        friend_friend = {"userid": f, "friendid": userid}
        message = {"userid": f, "type": "4", "content": u.nickname + " agree to add you"}

        try:
            with transaction.atomic():
                result = FriendDAO.new_friend(**friend_user)
                FriendDAO.new_friend(friend_friend)
                AddFriendDAO.delete_addfriend(addfriend_id)
                MessageDAO.new_message(**message)

        except IntegrityError:
            result = "error"

        return result

    # type = 2 represents refuse to add
    else:
        message = {"userid": f, "type": "4", "content": u.nickname + " refuse to add you"}
        try:
            with transaction.atomic():
                AddFriendDAO.delete_addfriend(addfriend_id)
                MessageDAO.new_message(**message)

        except IntegrityError:
            result = "error"

        return result





