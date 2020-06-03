#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 7.将序列分解为单独的变量.py
# @Software: PyCharm
records = [
    ('AAA', 1, 2),
    ('BBB', 'hello'),
    ('CCC', 5, 3)
]


def do_foo(x, y):
    print('AAA', x, y)


def do_bar(s):
    print('BBB', s)


# 迭代的records元素，取第一个，其余的变为*rest，意为可变长序列
for tag, *rest in records:
    if tag == 'AAA':
        do_foo(*rest)
    elif tag == 'BBB':
        do_bar(*rest)

line = 'guan:jing123://wef:678d:guan'
# 中间部分可辨长，头尾指定单独变量
uname, *fields, homedir, sh = line.split(':')
print(uname, homedir)
