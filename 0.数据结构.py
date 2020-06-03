#!/usr/bin/env python
# -*- coding: utf-8 -*-


# [object.h] python中所有的东西都被当做是对象来处理，这个对象源码是是object.h中定义的：PyObject
# python内建了垃圾回收机制, 引用计数是其中的一部分.
# 通过 Py_INCREF(op) 和 Py_DECREF(op) 两个宏来增加和较少引用计数，进行垃圾回收.



# 1.一个数的元组,(1)会被看作是数字
tp = (1,)
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

a, c = tup2
print(a, c)

# 修改元组是非法的
# tup1[0] = 100
# 使用del语句来删除整个元组
del tup1

# 2.字典，可以混搭
dict1 = {'user': 'test', 'num': [1, 2, 3]}  # 原字典
# 浅拷贝，只深拷贝父级目录
dict2 = dict1  # 直接赋值
dict3 = dict1.copy()
import copy

dict4 = copy.deepcopy(dict1)  # 深拷贝拷贝，父级目录，子级目录全部拷贝

# 3.set
strs = set(['jeff', 'wong', 'cnblogs'])
nums = set(range(10))
s = set([22, '的'])

# 4.list
a = ['sa', 'ass', 'vvv']
# .join效率会更高，只分配一次内存，+ai方式会分配 n-1词
print(','.join(a))
# len(list)：列表元素个数
# max(list)：返回列表元素最大值
# min(list)：返回列表元素最小值
# list(seq)：将元组转换为列表
#
# 方法:
# list.append(obj)：在列表末尾添加新的对象
# list.count(obj)：统计某个元素在列表中出现的次数
# list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
# list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
# list.insert(index, obj)：将对象插入列表
# list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
# list.remove(obj)：移除列表中某个值的第一个匹配项
# list.reverse()：反向列表中元素
# list.sort([func])：对原列表进行排序


# 5. str ,int
# 字符串对象的共享机制intern：小整数一样将段字符串作为共享其他变量引用，以达到节省内存和性能上不必要的开销，这就是intern机制
# inter机制的核心在 interned 变量中，interned = PyDict_New(); 也就是在python中经常用到的 dict 。
# 这样就很清楚了， 就是在系统中有一个（key，value）映射关系的集合。
# Objects/unicodeobject.c PyUnicode_InternInPlace
a = 'hello'
b = 3
print(a + str(b))
'''
使用 “+” 符号进行字符串拼接
[unicodeobject.c]
PyUnicode_Concat(PyObject *left, PyObject *right），
这种方法效率极低， 因为在python中PyUnicodeObject对象是一个不可变对象。
这就意味着当进行字符串拼接时，实际上是创建一个新的对象。如果要链接n个PyUnicodeObject对象，
就要进行n-1次内存申请和内存搬运的工作。因此，当需要多个字符串拼接时，官方推荐的做法是通过

join（）来操作。
[unicodeobject.c] Pyunicode_join(PyObject *self, PyObject *iterable)
这种做法只需要分配一次内存，执行效率大大提高。
'''


# 没有long,print(long(1))
# NameError: name 'long' is not defined
# print(long(1))

# Python支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
print(1 + 2j)
print(complex(1, 2) + complex(2, 3))

# 小数据池:str,int,bool。范围: -5~256
# 源文件：Objects/longobject.c
# #ifndef NSMALLPOSINTS
# #define NSMALLPOSINTS           257
# #endif
# #ifndef NSMALLNEGINTS
# #define NSMALLNEGINTS           5
# Python中一种提高效率的方式,固定数据类型使用同一个内存地址
# id 查看空间的内存地址
# 满足缓存机制则他们在内存中只存在一个
a = 22
b = 22
c = 'ss'
d = 'ss'
print(id(a), id(b), id(c), id(d))
# 4363130672 4363130672 4366738800 4366738800
# int(float):任何数字在同一代码块下都会复用。
# bool:True和False在字典中会以1，0方式存在，并且复用。
# str：几乎所有的字符串都会符合缓存机制
