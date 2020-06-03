#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:51
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 4hard.py
# @Software: PyCharm


# ------------例子2，执行顺序详细打印------------
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("range,i=", i)
        # 做一些其它的事情
    print("do something.")
    print("end.")


def call(i):
    print('call,i=', i)
    return i * 2


# 使用for循环
for i in yield_test(3):
    print('print,i=', i)
    print('-' * 20)
