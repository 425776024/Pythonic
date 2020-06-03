#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 11.heapq堆数据结构使用.py
# @Software: PyCharm

import heapq

'''
堆是二叉树，最大堆中父节点大于或等于两个子节点，最小堆父节点小于或等于两个子节点。
'''
print('创建，获取最小值。heap[0]', '-' * 50)
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
print('nums', nums)
for num in nums:
    heapq.heappush(heap, num)  # 加入堆
print('heap[0]:', heap[0])  # 只获取最小值，不是弹出
print()

print('创建，转换列表成为堆结构。heapq.heapify(nums)', '-' * 50)
print(nums)
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)  # 转成堆结构，nums改变
print(nums)
print([heapq.heappop(nums) for _ in range(len(nums))])  # 转成堆结构才能按顺序打印
print()

print('合并多个排序序列成一个排序序列，返回值的迭代器。nums=heapq.merge(nums1,nums2)')
nums1 = [2, 3, 5, 1, 54, 23, 132]
nums1 = sorted(nums1)
print('nums1', nums1)
nums2 = [22, 23, 25, 21, 254, 223, 2132]
nums2 = sorted(nums2)
print('nums2', nums2)
nums = heapq.merge(nums1, nums2)  # 值的迭代器
print('nums', list(nums))
print()

print('删除堆中最小元素并加入一个元素23。heapq.heaprepalce()')
nums = [1, 2, 4, 5, 3]
print('nums', nums)
heapq.heapreplace(nums, 23)
print([heapq.heappop(nums) for _ in range(len(nums))])
print()

print('最大/小的k个值。heapq.nlargest(3, nums)/heapq.nsmallest(3, nums)')
nums = [1, 3, 4, 5, 2, 9]
print(nums)
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))
