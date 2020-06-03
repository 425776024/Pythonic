#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 8.将序列最后几项作为历史记录.py
# @Software: PyCharm

from collections import deque


def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)  # 设置队列，最大长度
    for line in lines:
        if pattern in line:  # 只有匹配pattern时才yield返回，及其前面的历史记录
            yield line, previous_lines
        previous_lines.append(line)  # 记录所有历史记录，最大maxlen=history


lines = ['AA',
         'abbaAA',
         'ee',
         'ad',
         'a1AAsss',
         'skas',
         '1233',
         'salddsd',
         'sdsfw2q',
         'ddAAdd',
         '1AA1',
         'sAAss']

for line, previous_lines in search(lines, 'AA', history=3):
    for pline in previous_lines:
        print(pline, end=',')

    print('<前面是', line)
    print('-' * 20)
