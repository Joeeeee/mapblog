from django.db import models
import datetime
# Create your models here.


class User(models.Model):

    phone = models.CharField(max_length=20)

    password = models.CharField(max_length=16)

    info = models.CharField(max_length=300)

    sex = models.CharField(max_length=5, default="male")

    head = models.FileField(upload_to='./static/Upload/Head')

    nickname = models.CharField(max_length=30)

    age = models.CharField(max_length=3)

    last_longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)

    last_latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True)

    city = models.CharField(max_length=10)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.username) + ' ' + str(self.userid) + ' ' + str(self.password) + ' ' + \
               str(self.sex) + ' ' + str(self.head) + ' ' + str(self.nickname) + ' ' + str(self.age) + ' ' + \
               str(self.last_longitude) + ' ' + str(self.last_latitude) + ' ' + str(self.city)


class Photo(models.Model):

    photo1 = models.FileField(upload_to='./static/Upload/Photo')

    photo2 = models.FileField(upload_to='./static/Upload/Photo')

    photo3 = models.FileField(upload_to='./static/Upload/Photo')

    photo4 = models.FileField(upload_to='./static/Upload/Photo')

    photo5 = models.FileField(upload_to='./static/Upload/Photo')

    photo6 = models.FileField(upload_to='./static/Upload/Photo')

    photo7 = models.FileField(upload_to='./static/Upload/Photo')

    photo8 = models.FileField(upload_to='./static/Upload/Photo')

    photo9 = models.FileField(upload_to='./static/Upload/Photo')

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.blogid) + ' ' + str(self.photo1) + ' ' + str(self.photo2) + ' ' + \
               str(self.photo3) + ' ' + str(self.photo4) + ' ' + str(self.photo5) + ' ' + str(self.photo6) + ' ' + \
               str(self.photo7) + ' ' + str(self.photo8) + ' ' + str(self.photo9)


class Blog(models.Model):

    content = models.CharField(max_length=300)

    latitude = models.DecimalField(max_digits=10, decimal_places=3)

    longitude = models.DecimalField(max_digits=10, decimal_places=3)

    datetime = models.DateTimeField(default=datetime.datetime.now())

    blog_comment_count = models.CharField(max_length=10, default="0")

    blog_like_count = models.CharField(max_length=10, default="0")

    userid = models.ForeignKey(User)

    photoid = models.ForeignKey(Photo, null=True)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.content) + ' ' + str(self.latitude) + ' ' + str(self.longitude) + ' ' + \
               str(self.time) + ' ' + str(self.blog_comment_count) + ' ' + str(self.blog_like_count) + ' ' + \
               str(self.userid) + ' ' + str(self.photoid)


class Comment(models.Model):

    blogid = models.ForeignKey(Blog)

    datetime = models.DateTimeField(default=datetime.datetime.now())

    # 1 represents comment to blog, 2 represents comment to comment
    type = models.CharField(max_length=5, default="1")

    content = models.CharField(max_length=300)

    userid = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.date) + ' ' + str(self.type) + ' ' + str(self.content) + ' ' + \
               str(self.userid) + ' ' + str(self.date)


class Message(models.Model):

    userid = models.ForeignKey(User)

    content = models.CharField(max_length=100)

    type = models.CharField(max_length=5)

    isread = models.BooleanField(default=False)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.userid) + ' ' + str(self.content) + ' ' + str(self.type)


class Friend(models.Model):

    userid = models.ForeignKey(User)

    friendid = models.CharField(max_length=5)

    remark = models.CharField(max_length=30)

    # type: 1 represents is in black list, 0 represents not in the black list
    friend_type = models.CharField(max_length=5, default="0")

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.userid) + ' ' + str(self.friendid) + ' ' + str(self.remark) + ' ' + \
               str(self.friend_type)


class Addfriend(models.Model):

    userid = models.ForeignKey(User)

    friendid = models.CharField(max_length=5)

    datetime = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.userid) + ' ' + str(self.friendid) + ' ' + str(self.date)


class Group(models.Model):

    # who set up the group
    userid = models.ForeignKey(User)

    name = models.CharField(max_length=30, default="Group")

    member_count = models.CharField(max_length=5, default="0")

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.userid) + ' ' + str(self.name) + ' ' + str(self.member_count)


class Groupmember(models.Model):

    userid = models.ForeignKey(User)

    groupid = models.ForeignKey(Group)

    def __unicode__(self):
        return str(self.id) + ' ' + str(self.userid) + ' ' + str(self.groupid)


