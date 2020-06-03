#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 12:30
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 2start.py
# @Software: PyCharm
import threading
import asyncio
import time


async def hello(n):
    # 打印的currentThread是一样的，也就是自始自终就是一个线程在高
    print('Hello world! (%s)' % threading.currentThread())
    print(n)
    await asyncio.sleep(2)
    print('Hello again! (%s)' % threading.currentThread())


start = time.time()
loop = asyncio.get_event_loop()
# 3个coroutine是由同一个线程并发执行的。
tasks = [hello(3), hello(6), hello(7)]
# 一组的时候要加wait
# timeout指定超时
loop.run_until_complete(asyncio.wait(tasks, timeout=10))
loop.close()
print('time:', time.time() - start)
print('time打印的时间肯定远远低于3s！，但是我们执行了3个sleep(1)（耗时1s以上的函数）的操作')
