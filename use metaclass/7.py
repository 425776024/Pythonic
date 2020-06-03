#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 15:33
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 7.py
# @Software: PyCharm


class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        if 0 < age < 150:
            return object.__new__(cls)
            # return super(Person, cls).__new__(cls)
        else:
            return None


b = People('s', 100)
print(b)
b = People('s', 1010)
print(b)
