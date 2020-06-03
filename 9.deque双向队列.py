#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 1:13 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 9.deque双向队列.py
# @Software: PyCharm
from collections import deque

'''
deque是双向队列，底层用双链表实现
'''
print('创建，初始空，a=deque(maxlen=3)')
a = deque(maxlen=3)
print(a)
print()

print('创建，最大len=3，a=deque([1,2,3,4,5,6], maxlen=3)')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
print()

print('删除一个，最新来排队的那个(6)，a.pop()')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
a.pop()
print(a)
print()

print('删除一个，最早来排队的那个，a.popleft()')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
a.popleft()
print(a)
print()

print('查找第一个匹配到5的位置，a.index(5)')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
print(a.index(5))
print()

print('反过来排队，a.reverse()')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
a.reverse()
print(a)
print()

print('append添加一个，最新8进去，排队。a.append(8)')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
a.append(8)
print(a)
print()

print('extend添加一列，最新[8,88]进去，排队。a.extend([8,88])')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
a.extend([8, 88])
print(a)
print()

print('appendleft添加一个，最新8进去，插队到最前面。a.appendleft(8)')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
a.appendleft(8)
print(a)
print()

print('extendleft添加一列，最新[8,88]进去，插队到最前面。a.extendleft([8,88])')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print(a)
a.extendleft([8, 88])
print(a)
print()

print('深拷贝。b=a.copy()')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print('a', a)
b = a.copy()
b.append(999)
print('a', a)
print('b', b)
print()

print('浅拷贝。b=a')
a = deque([1, 2, 3, 4, 5, 6], maxlen=3)  # 创建：
print('a', a)
b = a
b.append(999)
print('a', a)
print('b', b)
print()
