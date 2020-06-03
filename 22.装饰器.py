#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 12:15 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 22.装饰器.py
# @Software: PyCharm
def funA(fn):
    print('A')
    fn()  # 执行传入的fn参数
    return 'fkit'


'''
下面装饰效果相当于：funA(funB)，
funB 将会替换（装饰）成 funA() 语句的返回值；
由于funA()函数返回 fkit，因此 funB 就是 fkit
'''


@funA
def funB():
    print('B')


# funA(funB) >print('A')>print('B')>return 'fkit'>print('fkit')
print(funB)

print('--' * 10)


# 取消装饰的定义
def funB():
    print('B')


print(funA(funB))

import time
from tqdm import tqdm


def statistic_time(func):
    import datetime
    start = datetime.datetime.now()

    def fun(*args, **kwargs):
        func(*args, **kwargs)

    end = datetime.datetime.now()
    print('函数:%s，耗时:%s' % (func.__name__, end - start))
    return fun


@statistic_time
def call(*args, **kwargs):
    bar = tqdm(range(10))
    for i in bar:
        bar.set_description('resault:' + str(args[0] + i + kwargs['fuck']))
        time.sleep(0.2)


call(10, 2, 3, 2, 3, 3, fuck=90)
