#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/3 16:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 3.setattr.py
# @Software: PyCharm

# 为对象添加变量或方法
def abc(self):
    print("%s正在交谈" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name


p = Person("laowang")
setattr(p, "talk", abc)  # 将abc函数添加到对象中p中，并命名为talk
p.talk(p)  # 调用talk方法，因为这是额外添加的方法，需手动传入对象

setattr(p, "age", 30)  # 添加一个变量age,复制为30
print(p.age)  # 打印结果:30
