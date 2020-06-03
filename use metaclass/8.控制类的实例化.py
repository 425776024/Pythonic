#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 15:45
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 8.控制类的实例化.py
# @Software: PyCharm

# 利用new，init控制实例化产生
class Mymeta(type):
    def __call__(self, *args, **kwargs):
        print(self)  # self是People
        print(args)  # args = ('nick',)
        print(kwargs)  # kwargs = {'age':18}
        # return 123
        # 1. 先造出一个People的空对象，申请内存空间
        # __new__方法接受的参数虽然也是和__init__一样，但__init__是在类实例创建之后调用，而 __new__方法正是创建这个类实例的方法。
        obj = self.__new__(self)  # 虽然和下面同样是People，但是People没有，找到的__new__是父类的
        # 2. 为该对空对象初始化独有的属性
        self.__init__(obj, *args, **kwargs)
        # 3. 返回一个初始化好的对象
        obj.name2 = 'haha'
        return obj


class People(object, metaclass=Mymeta):
    country = 'China'

    def __init__(self, name1, age):
        self.name1 = name1
        self.age = age

    def eat(self):
        print('%s is eating' % self.name1)


'''
类的调用，即类实例化就是元类的调用过程，可以通过元类Mymeta的__call__方法控制:
1.先造出一个People的空对象
2.为该对空对象初始化独有的属性
3.返回一个初始化好的对象
'''
p = People('name1', age=12)
p.eat()
print(p.name2)
