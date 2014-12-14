__author__ = 'Joeeee'

# -*- coding: utf-8 -*-

from blog.models import Comment

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


# basic operation
def publish_comment(**comment):
    result = Comment.object.create(**comment)
    return result


def delete_comment(comment_id):
    Comment.object.get(id=comment_id).delete()


def get_comment_by_id(comment_id):
    result = Comment.object.get(id=comment_id)
    return result


def update_comment(**comment):
    Comment.objects.filter(id=comment['id']).update(**comment)