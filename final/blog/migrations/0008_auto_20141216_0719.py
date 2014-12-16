# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20141216_0621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addfriend',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 7, 19, 8, 416340)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 7, 19, 8, 414125)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 16, 7, 19, 8, 414726)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo1',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo2',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo3',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo4',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo5',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo6',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo7',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo8',
            field=models.FileField(upload_to=b'Photo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='head',
            field=models.FileField(upload_to=b'Head'),
            preserve_default=True,
        ),
    ]
