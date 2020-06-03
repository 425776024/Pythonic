#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 2:38 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 22.staticmethod.py
# @Software: PyCharm
class cal:
    cal_name = '计算器'

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod  # 静态方法 类或实例均可调用
    def cal_test(a, b, c):  # 改静态方法函数里不传入self 或 cls
        print(a, b, c)
        # print(self.x) #压根没self，所以自然用不了
        # print(cal_name) #隐性self也用不了


c1 = cal(10, 11)

cal.cal_test(1, 2, 3)  # 直接不创建对象实例能用
c1.cal_test(1, 2, 3)  # 创建了也能用，不过不属于这个实例，这个是大家公用的
