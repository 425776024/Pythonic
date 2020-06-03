#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/31 12:41 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 6.下划线命名.py
# @Software: PyCharm
'''

python的几种下划线意义：

- 单前 `_var`：约定、非强制，起提示作用
- 单后 `var_`：约定、非强制，避免关键字
- 双前 `__var`：特殊意义，会触发修饰名称
- 前后 `__var__`：特殊方法定义
'''


# 变量中使用，能直接访问里面的变量
class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23


t = Test()
t.foo
# 11
t._bar
# 23


# 函数使用前下划线_ 的时候，从模块中*通配符*导入，既然报错
from python.my_module import *

external_func()
# 23
_internal_func()
# NameError: "name '_internal_func' is not defined"

# 函数使用，你看，前下划线的时候，从模块中指名道姓，才不会出问题
import python.my_module as module

module.external_func()
# 23
module._internal_func()
# 42


# 双前 `__var`：
# 特殊意义，会触发修饰名称，不能在外面直接访问

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23


# 会自动修饰 双前下划线变量 名称，变成 _Test__baz
t = Test()
dir(t)
'''
['_Test__baz', '__class__', '__delattr__', '__dict__', '__dir__',
 '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
 '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__module__',
 '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
 '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
 '__weakref__', '_bar', 'foo']
'''


# 继承之前的Test，全部重写变量定义
class ExtendedTest(Test):
    def __init__(self):
        super().__init__()
        self.foo = 'overridden'
        self._bar = 'overridden'
        self.__baz = 'overridden'


# 双前下划线变量 的无法：访问 重写，其它可以访问且被重写了
t2 = ExtendedTest()
t2.foo
'overridden'
t2._bar
'overridden'
t2.__baz
AttributeError: "'ExtendedTest' object has no attribute '__baz'"

# 查看变量，多了 _ExtendedTest__baz, _Test__baz
dir(t2)
'''
['_ExtendedTest__baz', '_Test__baz', '__class__', '__delattr__',
 '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
 '__getattribute__', '__gt__', '__hash__', '__init__', '__le__',
 '__lt__', '__module__', '__ne__', '__new__', '__reduce__',
 '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__', '_bar', 'foo', 'get_vars']

'''
# 可以这样访问
t2._ExtendedTest__baz
# 'overridden'
t2._Test__baz
# 42
