__author__ = 'Joeeee'

from blog.models import Addfriend

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


# basic operation
def new_addfriend(**addfriend):
    result = Addfriend.object.create(**addfriend)
    return result


def delete_comment(addfriend_id):
    Addfriend.object.get(id=addfriend_id).delete()


def get_addfriend_by_id(addfriend_id):
    result = Addfriend.object.get(id=addfriend_id)
    return result


def update_addfriend(**addfriend):
    Addfriend.objects.filter(id=addfriend['id']).update(**addfriend)