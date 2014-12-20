__author__ = 'Joeeee'

import datetime
from django.db.models.loading import get_model


# change model object to dict type
def todcit(model_obj):

    # model_obj = get_model('blog', model_name)

    fields = []
    # print model_obj._meta_fields

    for field in model_obj._meta.fields:
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

# from blog.Service import UserService
# from blog.DAO import UserDAO
# from blog.models import User
#
# print todcit(UserDAO.get_user_by_id(13))