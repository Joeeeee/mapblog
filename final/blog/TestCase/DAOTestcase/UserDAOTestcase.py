# -*- coding: utf-8 -*-
__author__ = 'Joeeee'


from django.test import TestCase
from blog.DAO import UserDAO
from blog.models import User
from django.core.files import File


# If your tests rely on database access such as creating or querying models,
# be sure to create your test classes as subclasses of django.test.TestCase rather than unittest.TestCase.
# Create your tests here.
# you can simulate requests, insert test data, inspect your application’s output and generally verify your code is doing
#  what it should be doing.

# from django.test import TestCase
# from myapp.models import Animal

# class AnimalTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')

# 怎么测试DAO
# 增加->查->修改->删除

# filter和get有什么不同
# get不存在的会报错，filter不存在的不会报错
# get得到的是对象，filter得到的是结果集

# However, a big part of the time taken to run a Django TestCase is consumed by the call to flush that ensures that you
# have a clean database at the start of each test run.
# django为我们在setting文件中database列出的每个数据库对应设置一个测试数据库
# 每个test开始的时候都会有一个全新的数据库（包含setUp的数据），执行test很大的一个时间开支用在flush数据库

# 每个DAO一个类去测试
class UserDAOTest(TestCase):
    def setUp(self):
        # 约定：假定django框架所给的都是值得信赖的
        # 约定：下面的测试函数可以使用上面测试过的函数
        # 约定：一个测试函数不可以使用另外一个测试函数新加的变量，只使用setup中设置的变量
        # 测试中要用到的全局在setUp这里设置

        # set default head photo
        f = open("/Upload/Head/head.png")
        head_photo = File(f)

        self.user = {"id":1, "phone": "18688282803", "password": "12345678", "info": "I am a boy", "sex": "male"}
        self.user2 = {"id":2,"password":"1234567","nickname":"frank2","photo":"this is a photo","phone":"111111112",
                      "contacts_version":"1.0","longitude":"1.23","latitude":"23.45","code":"111111112"}
        User.objects.create(**self.user)
        User.objects.create(**self.user2)

    # 加了之后的数量减去加了之前的数量等于1
    def test_insert_user(self):
        user3 = {"id":3,"password":"7654321","nickname":"frank3","photo":"this is a photo","phone":"111111111","contacts_version":"1.0","longitude":"1.23","latitude":"23.45","code":"111111113"}
        before = len(User.objects.all())
        UserDAO.new_user(**user3)
        after = len(User.objects.all())
        self.assertEqual(after-before,1)

    def test_get_user_by_id(self):
        self.assertEqual(UserDAO.get_user_by_id(1).id, 1)
        self.assertEqual(UserDAO.get_user_by_id(2).id,2)

    def test_update_user(self):
        modified_user = {"id":1,"password":"changed_password","nickname":"frank","photo":"this is a photo","phone":"13570517279","contacts_version":"1.0","longitude":"1.23","latitude":"23.45","code":"auto_generating_code"}
        UserDAO.update_user(**modified_user)
        self.assertEqual(UserDAO.get_user_by_id(1).password,"changed_password")

    def test_delete_user(self):
        UserDAO.delete_user(1)
        UserDAO.delete_user(2)
        self.assertEqual(len(User.objects.filter(id=1)), 0)
        self.assertEqual(len(User.objects.filter(id=2)), 0)





