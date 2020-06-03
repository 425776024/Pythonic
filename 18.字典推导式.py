#!/usr/bin/env python
# -*- coding: utf-8 -*-

mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}

print('mcase:', mcase)
print()
print('忽略key大小写，相加key的value，且过滤掉不是a,b的')
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.lower(), 0)
    for k in mcase.keys()
    if k.lower() in ['a', 'b']
}

print('mcase_frequency:', mcase_frequency)
print()
print('反转mcase的 k,v')
mcase_revers = {v: k for k, v in mcase.items()}
print(mcase_revers)
