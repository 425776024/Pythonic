#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'x': 11,
    'y': 2,
    'w': 10
}

print(a.keys() & b.keys())  # 公共键
print(a.keys() - b.keys())  # 差键
print(a.items() & b.items())  # 公共元素
c = {key: a[key] for key in a.keys() - {'z', 'w'}}  # 过滤，包含z,w不要
print(c)
