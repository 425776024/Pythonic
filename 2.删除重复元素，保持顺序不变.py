#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : 2.删除重复元素，保持顺序不变.py

def dedupe_iter(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [5, 5, 2, 1, 9, 1, 5, 10]
print(a)
print(list(dedupe_iter(a)))
it = dedupe_iter(a)
while True:
    try:
        c = next(it)
        print(c, end='//')
    except Exception  as e:
        print(e)
        break


# 复杂对象去重复
def buha(items, key=None):
    seen = set()
    for item in items:
        #  print(seen)
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 2, 'y': 3}, {'x': 1, 'y': 4},
     {'x': 2, 'y': 3}, {'x': 10, 'y': 15}]
print(a)
print(list(buha(a, key=lambda x: (x['x'], x['y']))))


# 自定义哈希
class Foo:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def __hash__(self):
        # 当两个变量的哈希值不相同时，就认为这两个变量是不同的。
        return hash(self.count)

    def __eq__(self, other):
        # 当两个变量哈希值一样时，调用__eq__方法，比较是否具有相同的各种属性，可以简单地理解为值是否相等
        # self是存在的一方对象，other是新来的和存在的冲突的对象
        if self.count == other.count:
            # if self.__dict__ == other.__dict__:
            return True
        else:
            return False

    def __repr__(self, ):
        return 'print:%s' % (self.name)


f1 = Foo('f1', 1)
f2 = Foo('f2', 2)
f3 = Foo('f3', 3)
f4 = Foo('f4', 3)
f5 = Foo('f5', 3)
f6 = Foo('f6', 3)
ms = [f1, f2, f3, f4, f5, f6]
print(set(ms))
