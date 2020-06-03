#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 5:51 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 25.Python垃圾回收.py
# @Software: PyCharm
'''

###导致引用计数+1的情况

- `对象被创建，例如a=23`
- `对象被引用，例如b=a`
- `对象被作为参数，传入到一个函数中，例如func(a)`
- `对象作为一个元素，存储在容器中，例如list1=[a,a]`



###导致引用计数-1的情况

- `对象的别名被显式销毁，例如del a`
- `对象的别名被赋予新的对象，例如a=24`
- `一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）`
- `对象所在的容器被销毁，或从容器中删除对象`
'''
import gc
import sys

a = []
b = []
a.append(b)
print('a refcount:', sys.getrefcount(a))  # 2
print('b refcount:', sys.getrefcount(b))  # 3

# ==========================
import gc


class ClassA():
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))))


def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2


# 把python的gc关闭
# gc.disable()
# 执行f2()，进程占用的内存会不断增大。
# f2()

# =============================
import gc


class ClassA():
    def __init__(self):
        print('object born,id:%s' % str(hex(id(self))))

    def __del__(self):
        print('object del,id:%s' % str(hex(id(self))))


'''
垃圾回收后的对象会放在gc.garbage列表里面
gc.collect()会返回不可达的对象数目，4等于两个对象以及它们对应的dict
'''


def f3():
    print("-----0------")
    # print(gc.collect())
    c1 = ClassA()
    c2 = ClassA()
    c1.t = c2
    c2.t = c1
    print("-----1------")
    del c1
    del c2
    print("-----2------")
    print(gc.garbage)
    print("-----3------")
    print(gc.collect())  # 显式执行垃圾回收
    print("-----4------")
    print(gc.garbage)
    print("-----5------")


if __name__ == '__main__':
    # gc.set_debug(gc.DEBUG_LEAK)  # 设置gc模块的日志
    f3()
