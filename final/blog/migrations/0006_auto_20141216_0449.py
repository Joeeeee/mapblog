# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20141216_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 4, 49, 22, 162850)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 4, 49, 22, 160605)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 4, 49, 22, 161210)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default=b'GUANGZHOU', max_length=30),
            preserve_default=True,
        ),
    ]
