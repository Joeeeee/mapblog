# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

from django.db import transaction
from django.db.transaction import DatabaseError
from django.db import IntegrityError
from blog.DAO import UserDAO
from blog.DAO import BlogDAO

import datetime


# user publish a new blog
def newblog(userid, content, longitude, latitude):

    # get user instance by userid, then use to blog foreign key
    try:
        u = UserDAO.get_user_by_id(userid)
    except DatabaseError:
        return None

    # object create
    new_blog = {"content": content, "longitude": longitude, "latitude": latitude, "datetime": datetime.datetime.now(),
                "userid": u}

    try:
        result = BlogDAO.insert_blog(**new_blog)
    except IntegrityError:
        result = None

    return result
