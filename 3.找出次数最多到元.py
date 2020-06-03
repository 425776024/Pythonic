#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 12:23 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 3.找出次数最多到元.py
# @Software: PyCharm
from collections import Counter

words = ['look', 'info', 'my', 'AAA', 'look', 'my', 'AAA', 'the', 'AAA', 'the', 'AAA', 'the', 'eyes', 'not', 'BBB',
         'the',
         'AAA', 'dont', 'BBB', 'around', 'the', 'AAA', 'look', 'into', 'BBB', 'AAA', 'under']

words_counts = Counter(words)
# 最多频率的3个元组
top_3 = words_counts.most_common(3)
print(words_counts)
print()
print('top_3:\n', top_3)

# Counter其它操作
from collections import Counter

print('c.subtract(d)')
c = Counter(a=4, b=2, c=0, d=-2)
print(c)
d = Counter(a=1, b=2, c=3, d=4, e=11)
print(d)
c.subtract(d)  # 相减
print(c)

print('c+d', '-' * 50)
c = Counter(a=4, b=2, c=0, d=-2, e=11)
print(c)
d = Counter(a=1, b=2, c=3, d=4)
print(d)
print(c + d)  # 相加，舍去非正数

print('c-d', '-' * 50)
c = Counter(a=4, b=2, c=0, d=-2, e=11)
print(c)
d = Counter(a=1, b=2, c=3, d=4)
print(d)
print(c - d)  # 相减，舍去非正数

print('c&d', '-' * 50)
c = Counter(a=4, b=2, c=0, d=-2, e=11)
print(c)
d = Counter(a=1, b=2, c=3, d=4)
print(c & d)  # 交集，取小的那个，舍去非正数

print('c|d', '-' * 50)
c = Counter(a=4, b=2, c=0, d=-2, e=11)
print(c)
d = Counter(a=1, b=2, c=3, d=4)
print(d)
print(c | d)  # 并集，取大的那个，舍去非正数

print('c.update(d)', '-' * 50)
c = Counter(a=4, b=2, c=0, d=-2, e=11)
print(c)
d = Counter(a=1, b=2, c=3, d=4)
print(d)
c.update(d)  # 更新Counter，对于已有的元素计数加对应新的数量，对没有的元素进行添加
print(c)

print('-' * 50)
print(c.items())
print(list(c))
print(set(c))
print(dict(c))
print(c.values())
