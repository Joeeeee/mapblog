__author__ = 'Joeeee'

from blog.models import Message

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


# basic operation
def new_message(**message):
    result = Message.object.create(**message)
    return result


def delete_message(message_id):
    Message.object.get(id=message_id).delete()


def get_message_by_id(message_id):
    result = Message.object.get(id=message_id)
    return result


def update_message(**message):
    Message.objects.filter(id=message['id']).update(**message)