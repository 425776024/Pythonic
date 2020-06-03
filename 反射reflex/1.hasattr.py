#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 16:34
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1.hasattr.py
# @Software: PyCharm
# 判断对象中是否有这个方法或变量

class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("%s正在交谈" % self.name)


p = Person("laowang")
print(hasattr(p, "talk"))  # True。因为存在talk方法
print(hasattr(p, "name"))  # True。因为存在name变量
print(hasattr(p, "abc"))  # False。因为不存在abc方法或变量
