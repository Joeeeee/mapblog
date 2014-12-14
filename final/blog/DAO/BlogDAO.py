__author__ = 'Joeeee'

# -*- coding: utf-8 -*-

from blog.models import Blog

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


# basic operation
def insert_blog(**blog):
    result = Blog.objects.create(**blog)
    return result


def delete_blog(blog_id):
    Blog.objects.get(id=blog_id).delete()


def get_blog(blog_id):
    result = Blog.objects.get(id=blog_id)
    return result


def update_blog(**blog):
    Blog.objects.filter(id=blog['id']).update(**blog)
