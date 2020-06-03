#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 2medium.py
# @Software: PyCharm

# 字符串
astr = 'ABC'
# 列表
alist = [1, 2, 3]
# 字典
adict = {"name": "wangbm", "age": 18}
# 生成器
agen = list((i for i in range(4, 8)))


def gen_yield(*args, **kw):
    '''
    :desc yield
    :param args:
    :param kw:
    :return:
    '''
    for item in args:
        for i in item:
            yield i


def gen_yield_from(*args, **kw):
    '''
    :desc yield from
    :param args:
    :param kw:
    :return:
    '''
    # 细微差别看到了吗？yield from能迭代集合里面的数据
    for item in args:
        yield from item


new_list = gen_yield(astr, alist, adict, agen)
new_list_2 = gen_yield_from(astr, alist, adict, agen)
print(list(new_list))
print(list(new_list_2))
