# -*- coding: utf-8 -*-
__author__ = 'Joeeee'

# 从数据库中获取特定的blog, 根据blog的时间进行排序
# from blog.DAO import BlogDAO
# r = []
# result = BlogDAO.get_blog_by_userid(15)
# for i in range(0, len(result)):
#     r.append(result[i])
#
# r.sort(lambda x, y: cmp(x.datetime, y.datetime))
#
# from blog.Utils import GenerateObject
# 把userid去掉
# r = GenerateObject.todcit(r[1])
# r.pop("userid")
# print r