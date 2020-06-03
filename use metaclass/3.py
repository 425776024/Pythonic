#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 12:27
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 3.py
# @Software: PyCharm

'''
创建类的3个要素：类名，基类，类的名称空间
People = type(类名，基类，类的名称空间)
'''
class_name = 'People'  # 类名

class_bases = (object,)  # 基类

# 类的名称空间
class_dic = {}
class_body = """
country='China'
def __init__(self,name,age):
    self.name=name
    self.age=age
def eat(self):
    print('%s is eating' %self.name)
"""

exec(
    class_body,
    {},
    class_dic,
)

# 类的3要素
print(class_name)
print(class_bases)
print(class_dic)

# 这样创建类
People_class = type(class_name, class_bases, class_dic)
print(People_class)

# 使用类
o_p = People_class('jjj', 12)
o_p.eat()
