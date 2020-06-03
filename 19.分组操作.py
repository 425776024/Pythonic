#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 10:02 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 19.分组操作.py
# @Software: PyCharm
from itertools import groupby
from operator import itemgetter

# 希望按日期分组,(如果things中分组key不连续，需要先排序，因为groupby是按照连续项进行分组)
things = [('2012-05-21', 11), ('2012-05-21', 3),
          ('2012-05-22', 10), ('2012-05-22', 4), ('2012-05-22', 22),
          ('2012-05-23', 33)]

# 日期，itemgetter(0)为group key，此时要保证其是排序好的
for key, items in groupby(things, itemgetter(0)):
    print('group key:', key)
    print('items:')
    for subitem in items:
        print(subitem)
    print('-' * 20)
