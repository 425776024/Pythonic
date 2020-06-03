#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 5:28 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 24.上下文变量.py
# @Software: PyCharm
import contextvars
import asyncio

val = contextvars.ContextVar('var', default='0')


async def setval():
    val.set('1')
    print(val.get())


async def printval():
    print(val.get())


asyncio.run(setval())
asyncio.run(printval())
print(val.get())
