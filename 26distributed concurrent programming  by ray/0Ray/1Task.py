#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:17
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1Task.py
# @Software: PyCharm

import ray
import time

ray.init()


@ray.remote
def f(i):
    time.sleep(1)
    return i


futures = [f.remote(i) for i in range(4)]
print(ray.get(futures))
