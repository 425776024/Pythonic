#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 11:55
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 5超时.py
# @Software: PyCharm
import asyncio


async def eternity():
    # Sleep for one hour
    await asyncio.sleep(3600)
    print('yay!')


async def main():
    # Wait for at most 1 second
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout!')


asyncio.run(main())
