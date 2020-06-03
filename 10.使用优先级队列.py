#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 10.使用优先级队列.py
# @Software: PyCharm
import heapq


class PriorityQueue:
    def __init__(self):
        # 队列数据存放变量
        self._queue = []
        # 事例化对象索引值，以便用于排序
        self._index = 0

    def push(self, item, priority):
        # 往（优先）队列中加数据
        # 以元组为判断依据，（优先级变量priority为负，实现优先级高到低优先级排序），
        # 元组第一个相同时，才会比较第二位（self._index）的值，其自增长，以保证顺序和加入顺序相同；第3为才是真正的数据
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        # 取弹出数据元组的最后一位(-priority,self._index,item)，item位对象的数据
        # return heapq.heappop(self._queue)[2]
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        # 以便于自动被print打印
        return 'Item:{}'.format(self.name)


q = PriorityQueue()
q.push(Item('AAA'), 1)
q.push(Item('BBB'), 9)
q.push(Item('CCC'), 5)
q.push(Item('DDD'), 3)
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
