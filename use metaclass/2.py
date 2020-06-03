#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 12:26
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 2.py
# @Software: PyCharm
class People:  # People=type(...)
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating' % self.name)


print(type(People))
