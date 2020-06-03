#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 13:29
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 4.自定义.py
# @Software: PyCharm
class Mymeta(type):
    # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __init__(self, class_name, class_bases, class_dic):
        print('self:', self)  # 现在是People
        print('class_name:', class_name)
        print('class_bases:', class_bases)
        print('class_dic:', class_dic)
        # 重用父类type的功能
        super(Mymeta, self).__init__(class_name, class_bases,
                                     class_dic)


class People(object, metaclass=Mymeta):
    # People=Mymeta(类名,基类们,类的名称空间)
    country = 'China'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating' % self.name)


# People的信息会被送到Mymeta元类中去：(类名,基类们,类的名称空间)
p = People('kk', 12)
p.eat()
