#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 10:57
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 4并发运行.py
# @Software: PyCharm
import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main1():
    # 虽然是用了协程，但是是串行的task，所有要3S，普通函数调用效果一样
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")


async def main2():
    # 2比上面的1要快1s，因为是并行的。之花最多的那个2S
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


# asyncio.run(main1())
asyncio.run(main2())
