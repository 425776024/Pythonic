#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 10:19 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 20.ChainMap多个字典映射合并为单个.py
# @Software: PyCharm
from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 相同key时，取前面的字典对象的value
c = ChainMap(a, b)
print(c)
print(c['x'])
print(c['y'])
print(c['z'])
print(list(c.keys()))
print((list(c.values())))
