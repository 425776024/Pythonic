#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 16:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 4.delattr.py
# @Software: PyCharm

# 删除对象中的变量。注意：不能用于删除方法
class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("%s正在交谈" % self.name)


p = Person("laowang")

delattr(p, "name")  # 删除name变量
print(p.name)  # 此时将报错
