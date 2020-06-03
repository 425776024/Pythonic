#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 12:24
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1start.py
# @Software: PyCharm

# asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
import asyncio


async def hello():
    print("Hello world!")
    # 把asyncio.sleep(1)看成是一个耗时1秒的IO操作，在此期间，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行。
    await asyncio.sleep(1)
    print("Hello again!")


# 运行，方式1
# # 获取EventLoop:
# loop = asyncio.get_event_loop()
# # 执行coroutine
# loop.run_until_complete(hello())
# loop.close()

# 方式2
asyncio.run(hello())
