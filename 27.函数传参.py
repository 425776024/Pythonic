#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 6:02 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 27.函数传参.py
# @Software: PyCharm

def func(*args, **kw):
    print('args', args)
    print('kw', kw)


# 无变量，有变量
func([1, 2, 3], 'aa', a='a', b='b')
