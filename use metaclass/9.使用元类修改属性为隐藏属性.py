#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 16:01
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 9.使用元类修改属性为隐藏属性.py
# @Software: PyCharm
class Mymeta(type):
    def __init__(self, class_name, class_bases, class_dic):
        # 加上逻辑，控制类Foo的创建
        super(Mymeta, self).__init__(class_name, class_bases, class_dic)

    def __call__(self, *args, **kwargs):
        # 加上逻辑，控制Foo的调用过程，即Foo对象的产生过程
        obj = self.__new__(self)
        self.__init__(obj, *args, **kwargs)
        # 修改属性为隐藏属性
        obj.__dict__ = {
            '_%s__%s' % (self.__name__, k): v
            for k, v in obj.__dict__.items()
        }

        return obj


class Foo(object, metaclass=Mymeta):  # Foo = Mymeta(...)
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


obj = Foo('nick', 18, 'male')
print(obj.__dict__)
