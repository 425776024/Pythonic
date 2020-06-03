#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 21:28
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 3async def 函数.py
# @Software: PyCharm

import asyncio


async def add(x, y):
    r = x + y
    return r


async def bad_call(a, b, c, d):
    a_b = await add(a, b)
    await asyncio.sleep(1)
    c_d = await add(c, d)
    print(a_b * c_d)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bad_call(1, 2, 3, 4))
