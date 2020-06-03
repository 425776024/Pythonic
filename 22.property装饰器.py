#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 1:58 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 22.property装饰器.py
# @Software: PyCharm
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2014 - self._birth


s = Student()
s.birth = 20
print(s.birth, s.age)
