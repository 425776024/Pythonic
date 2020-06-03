#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 5:53 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 26.pickle.py
# @Software: PyCharm
import pickle

d = dict(name='Bob', age=20, score=88)
bts = pickle.dumps(d)
print(type(bts))  # 输出：<type 'str'>

# 加载方式，读取bytes
bj2 = pickle.loads(bts)
print(type(obj2))  # 输出：<type 'tuple'>   
print(obj2)  # 输出：d {'age': 20, 'score': 88, 'name': 'Bob'}


# 文件
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
#d {'age': 20, 'score': 88, 'name': 'Bob'}