#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 11:38
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 3what.py
# @Software: PyCharm

g = (i for i in (1, 2, 3, 6))
print(type(g))
# error
# print(g[2])
print(next(g))
print(next(g))
print(next(g))
print(next(g))


def gen():
    x = yield 1
    print('x:', x)
    y = yield 2
    print('y:', y)
    yield 'end'


'''
generator.send(value)
作用：向生成器发送一个值，随后恢复执行。
value 参数是 send 方法向生成器发送的值，这个值会作为当前所在的 yield 表达式的结果

g.send(None) 和 next(g) 等价
'''

g = gen()
# or next(g)
ret = g.send(None)
# 或者写成 next(g)，这是激活生成器的推荐写法
print('第一次 yield 的返回值：', ret)
print('啪啪啪啪')

ret = g.send('测试1')
print('第二次 yield 的返回值：', ret)
print()
print('啪啪啪啪哔哔哔哔')
ret = g.send('测试2')
print('第3次 yield 的返回值：', ret)
