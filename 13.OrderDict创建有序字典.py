#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import OrderedDict

'''
先添加的 key-value 对排在前面，后添加的 key-value 对排在后面。这么个顺序。而不是按内部key自动排序
维护双向链表，内存是普通字典2倍
'''

odic = OrderedDict()

odic['k1'] = 'a'
odic['k2'] = 'dab'
odic['k3'] = 'c'
print('odic:', odic)

# 按照第2位（value值）进行排序：lambda oi: oi[1]
sort_od = OrderedDict(sorted(odic.items(), key=lambda oi: oi[1]))
print('sort_od:', sort_od)
