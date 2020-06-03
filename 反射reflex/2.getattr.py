#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 16:35
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 2.getattr.py
# @Software: PyCharm

# 获取对象中的方法或变量的内存地址
class Person(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("%s正在交谈" % self.name)


p = Person("laowang")

n = getattr(p, "name")  # 获取name变量的内存地址
print(n)  # 此时打印的是:laowang

f = getattr(p, "talk")  # 获取talk方法的内存地址
f()  # 调用talk方法

# 我们发现getattr有三个参数，那么第三个参数是做什么用的呢?
s = getattr(p, "abc", "not find")
print(s)
