__author__ = 'Joeeee'

from blog.models import Photo

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final.settings")

import django
django.setup()


# basic operation
def new_photo(**photo):
    result = Photo.object.create(**photo)
    return result


def delete_photo_by_id(photo_id):
    Photo.object.get(id=photo_id).delete()


def get_photo_by_id(photo_id):
    result = Photo.object.get(id=photo_id)
    return result


def update_photo(**photo):
    Photo.objects.filter(id=photo['id']).update(**photo)