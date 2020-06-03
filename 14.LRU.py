#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


# 基于orderedDict实现
class LRUCache(collections.OrderedDict):
    '''
    function:利用collection.OrdereDict数据类型实现:最近最少使用的算法
    OrdereDict有个特殊的方法popitem(Last=False)时则实现队列，弹出最先插入的元素
    而当Last=True则实现堆栈方法，弹出的是最近插入的那个元素。
    实现了两个方法：get(key)取出键中对应的值，若没有返回None
    set(key,value)更具LRU特性添加元素
    '''

    def __init__(self, size=5):
        self.size = size
        self.cache = collections.OrderedDict()  # 有序字典

    def get(self, key):
        if key in self.cache.keys():
            # 因为在访问的同时还要记录访问的次数（顺序）
            value = self.cache.pop(key)
            # 保证最近访问的永远在list的最后面
            self.cache[key] = value
            return value
        else:
            value = None
            return value

    def set(self, key, value):
        if key in self.cache.keys():  # 存在就移除，然后插入新值
            self.cache.pop(key)
            self.cache[key] = value
        elif self.size == len(self.cache):
            # 满了，弹出最老的数据，插入新的
            self.cache.popitem(last=False)
            self.cache[key] = value
        else:
            self.cache[key] = value


if __name__ == '__main__':
    test = LRUCache()
    test.set('a', 1)
    test.set('b', 2)
    test.set('c', 3)
    test.set('d', 4)
    test.set('e', 5)
    print(test.get('a'))
