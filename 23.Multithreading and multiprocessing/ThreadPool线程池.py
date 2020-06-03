#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 3:11 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : ThreadPool.py
# @Software: PyCharm
from multiprocessing.pool import ThreadPool
import time


def run(data):
    name = data[0]
    v = data[1]
    a = v ** 2
    print(name, v, a)
    # return i # return和不return对进程池运行速度会有比较大影响，不return效率更高


def thread_pool(num):
    p = ThreadPool(num)
    start_time = time.time()
    data = zip(['a', 'b', 'c'], [1, 3, 6])
    ret = p.map(run, data)
    p.close()
    p.join()
    print("thread_pool  %d, costTime: %fs ret.size: %d" % (num, (time.time() - start_time), len(ret)))


if __name__ == "__main__":
    # 5个线程，处理10个run计算任务
    thread_pool(5)
