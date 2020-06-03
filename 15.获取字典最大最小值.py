#!/usr/bin/env python
# -*- coding: utf-8 -*-
price = {
    '小米': 899,
    '三星': 3999,
    '华为': 1999,
    '苹果': 5000
}

print(min(price))  # 明显不对，因为是以key为判断的，需要反转key,value的关系
print(min(zip(price.values(), price.keys())))
print(max(zip(price.values(), price.keys())))

print(min(zip(price.values(), price.keys()))[1])
print(max(zip(price.values(), price.keys()))[1])
