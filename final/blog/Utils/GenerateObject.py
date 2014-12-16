__author__ = 'Joeeee'

import datetime
from django.db.models.loading import get_model


# change model object to dict type
def todcit(model_name):

    model_obj = get_model('blog', model_name)

    fields = []

    for field in model_obj._meta_fields:
        fields.append(field.name)

    d = {}
    for attr in fields:
            if isinstance(getattr(model_obj, attr),datetime.datetime):
                d[attr] = getattr(model_obj, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(model_obj, attr),datetime.date):
                d[attr] = getattr(model_obj, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(model_obj, attr)

    return d

