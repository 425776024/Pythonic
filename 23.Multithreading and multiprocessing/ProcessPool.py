#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 4:03 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : ProcessPool.py
# @Software: PyCharm
from multiprocessing import Pool as ProcessPool
import time


def run(data):
    name = data[0]
    v = data[1]
    a = v ** 2
    print(name, v, a)


def process_pool(num):
    p = ProcessPool(num)
    start_time = time.time()
    data = zip(['a', 'b', 'c'], [1, 3, 6])
    ret = p.map(run, data)
    p.close()
    p.join()
    print("process_pool %d, costTime: %fs ret.size: %d" % (num, (time.time() - start_time), len(ret)))


if __name__ == "__main__":
    process_pool(4)
