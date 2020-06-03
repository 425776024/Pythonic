#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 15:32
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 6.py
# @Software: PyCharm

class Foo:
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)
        print('__call__实现了，实例化对象可以加括号调用了')


obj = Foo()
obj('nick', age=18)

