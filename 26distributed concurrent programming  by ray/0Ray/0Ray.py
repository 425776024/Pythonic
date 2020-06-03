#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 17:40
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 0Ray.py
# @Software: PyCharm

import ray
import time

# Start Ray. If you're connecting to an existing cluster, you would use
# ray.init(address=<cluster-address>) instead.
# 指定内存大小
ray.init(object_store_memory=78643200)


# ray.init(redis_address="192.168.2.220:6379")


def f1():
    time.sleep(1)


@ray.remote(num_cpus=4)
def f2():
    time.sleep(1)


# 以下需要十秒。
time1 = time.time()
[f1() for _ in range(4)]
print(time.time() - time1)

# 以下需要一秒(假设系统至少有4个CPU)。//接近核数，效果最好
time2 = time.time()
ray.get([f2.remote() for _ in range(4)])
print(time.time() - time2)
