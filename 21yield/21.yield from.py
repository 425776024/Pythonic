#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 11:27 AM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 21.yield from.py
# @Software: PyCharm




# 子生成器
def average_gen():
    total = 0
    count = 0
    average = 0
    while True:
        new_num = yield average
        count += 1
        total += new_num
        average = total / count


# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()


# 调用send，向yield 传值 赋给 new_num
def main():
    calc_average = proxy_gen()
    next(calc_average)  # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0 Ps:10/1
    print(calc_average.send(20))  # 打印：15.0 Ps:10+20 / 2
    print(calc_average.send(30))  # 打印：20.0 Ps:10+20+30 / 3


main()
