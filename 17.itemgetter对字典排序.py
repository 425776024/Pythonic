#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 9:18 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 17.itemgetter对字典排序.py
# @Software: PyCharm
from operator import itemgetter

print('获得第1,2序号元素。b=itemgetter(1,2)')
a = [1, 2, 3]
b = itemgetter(1, 2)
print(b(a))
print()

rows = [
    {'fname': 'AAA', 'lname': 'ZHANG', 'uid': 1001},
    {'fname': 'CCC', 'lname': 'WU', 'uid': 1004},
    {'fname': 'BBB', 'lname': 'ZHOU', 'uid': 1002},
    {'fname': 'DDD', 'lname': 'LI', 'uid': 1003}
]

print('rows:', rows)

print('rows_by_fname=sorted(rows,key=itemgetter(\'fname\'))')
rows_by_fname = sorted(rows, key=itemgetter('fname'))
print('rows_by_fname:', rows_by_fname)
print()

print('rows_by_uid=sorted(rows,key=itemgetter(\'uid\'))')
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print('rows_by_uid:', rows_by_uid)
print()

print('rows_by_fname=sorted(rows,key=lambda r:r[\'fname\'])')
# 也可以传统对lambda，但是，据说itemgetter比lambda更快
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print('rows_by_fname:', rows_by_fname)
