from django.db import models
import datetime

# Create your models here.


class User(models.Model):

    username = models.CharField(max_length=30)

    userid = models.CharField(max_length=16)

    password = models.CharField(max_length=16)

    def __unicode__(self):
        return str(self.id) + ' ' + self.username + ' ' + self.userid + ' ' + self.password


class Blog(models.Model):

    content = models.CharField(max_length=300)

    latitude = models.CharField(max_length=10)

    longitude = models.CharField(max_length=10)

    userid = models.ForeignKey(User, null=True)

    time = models.DateTimeField()




