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
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())
    return n


start = time.time()
loop = asyncio.get_event_loop()

# 创建任务数组
tasks = [hello(3), hello(6), hello(7)]
# 弄成协程形式的task
tasks_res = loop.create_task(asyncio.wait(tasks))
# 开始循环event
loop.run_until_complete(tasks_res)
loop.close()

# 打印结果/顺序和原来可能不一样，不一定是：3,6,7
for si in tasks_res.result()[0]:
    print(si.result())
