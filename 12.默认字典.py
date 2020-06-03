#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import defaultdict

i = defaultdict(int)
print(i['a'])
print(i['b'])

# 默认字典类型，不存在的key为空的默认类型value
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(1)
print('d:', d)
print('d[\'a\']:', d['a'])
print('这个不存在：')
print('d[\'bbb\']:', d['bbb'])

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(1)
print(d)
