#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 12:24
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

cmd = """
x=1
print('exec函数运行了')
def func(self):
    pass
"""
class_dic = {}
# 执行cmd中的代码，然后把产生的名字丢入class_dic字典中
exec(cmd, {}, class_dic)
print(class_dic)