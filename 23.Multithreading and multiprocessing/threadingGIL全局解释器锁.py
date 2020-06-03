#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 4:08 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : GIL全局解释器锁.py
# @Software: PyCharm
import threading

global_num = 0
lock = threading.Lock()


def func1():
    global global_num
    lock.acquire()
    for i in range(1000000):
        global_num += 1
    lock.release()

    print("test1", global_num)


def func2(a, name, value):
    print(a, name, value)
    global global_num
    lock.acquire()
    for i in range(1000000):
        global_num += 1
    lock.release()

    print("test2", global_num)


if __name__ == '__main__':
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2, args=(2,), kwargs={'name': 2, 'value': 88})
    t1.start()
    t2.start()
