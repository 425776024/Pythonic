#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 5.使用列表推导式.py


# only if
squares = [x for x in range(10) if x % 2 == 0]
print(squares)
# if and else
squares = [x if x % 2 == 0 else -1 for x in range(10)]
print(squares)

values = ['1', '2', 'A', '3', '-', 'N/A']


def is_int(a):
    try:
        x = int(a)
        return True
    except ValueError:
        return False


print('列表推导', '-' * 50)
int_values2 = [v for v in values if is_int(v)]
print(int_values2)
