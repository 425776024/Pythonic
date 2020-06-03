#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 1.python布隆过滤器.py


#   安装：pip install pybloom-live
from pybloom_live import BloomFilter

# capacity是容量, error_rate 是能容忍的误报率
f = BloomFilter(capacity=1000, error_rate=0.001)

# 返回False，一定不存在/返回True，则有可能存在
state = f.add('你好')

# ScalableBloomFilter:自动扩容
from pybloom_live import ScalableBloomFilter

# SMALL_SET_GROWTH，扩容规则
sbf = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
sbf.add()  # 与BloomFilter 同
