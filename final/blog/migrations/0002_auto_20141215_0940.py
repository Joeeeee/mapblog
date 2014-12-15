# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmember',
            name='test222',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(default=b'GUANGZHOUG', max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default=b'male', max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 40, 19, 527244)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 40, 19, 525003)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 15, 9, 40, 19, 525655)),
            preserve_default=True,
        ),
    ]
