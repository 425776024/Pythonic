#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 3:36 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : DummyPool线程池.py
# @Software: PyCharm
from multiprocessing.dummy import Pool as DummyPool
import time


def run(data):
    name = data[0]
    v = data[1]
    a = v ** 2
    print(name, v, a)
    # return i # return和不return对进程池运行速度会有比较大影响，不return效率更高


def dummy_pool(num):
    p = DummyPool(num)
    start_time = time.time()
    data = zip(['a', 'b', 'c'], [1, 3, 6])
    ret = p.map(run, data)
    p.close()
    p.join()
    print("dummy_pool   %d, costTime: %fs ret.size: %d" % (num, (time.time() - start_time), len(ret)))


if __name__ == "__main__":
    dummy_pool(4)
