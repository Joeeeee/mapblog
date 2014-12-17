# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

from django.db import transaction
from django.db import IntegrityError
from blog.models import Blog
from blog.DAO import BlogDAO

import datetime


# user publish a new blog
def newblog(userid, content, longitude, latitude):

    # object create
    new_blog = {"content": content, "logitude": longitude, "latitude": latitude, "datetime": datetime.datetime.now(),
                "userid": userid}

    try:
        result = BlogDAO.insert_blog(**new_blog)
    except IntegrityError:
        result = None

    return result
