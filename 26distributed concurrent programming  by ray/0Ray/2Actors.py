#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:18
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 2Actors.py
# @Software: PyCharm

import ray

ray.init()


@ray.remote
class Counter(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        self.n += 1

    def read(self):
        return self.n


counters = [Counter.remote() for i in range(4)]
[c.increment.remote() for c in counters]
futures = [c.read.remote() for c in counters]
print(ray.get(futures))
