#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1easy.py
# @Software: PyCharm

def pre():
    yield 1
    yield 2
    yield 3
    yield 4

#定义3个迭代器，就可以不重复各自执行各自的迭代了哈哈哈哈

abc = pre()
a=list(abc)
print('****',a)

abc1=pre()
print(list(abc1))  # 一直迭代直到完

abc2=pre()
print(next(abc2))  # 迭代1次
for i in range(4):
    print(next(abc2))
