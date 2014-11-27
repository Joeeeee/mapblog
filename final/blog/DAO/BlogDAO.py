__author__ = 'Joeeee'

# -*- coding: utf-8 -*-

from blog.models import Blog

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


def insert_blog(**blog):
    b = Blog.objects.create(**blog)
    return b


def delete_blog(blog_id):

    Blog.objects.get(id=blog_id).delete()


def get_blog(blog_id):

    return Blog.objects.get(id=blog_id)


def update_blog(**blog):
    Blog.objects.filter(id=blog['id']).update(**blog)
