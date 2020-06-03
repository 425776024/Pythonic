#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : 4.排序类定义的实例.py
# @Software: PyCharm


class User:
    def __init__(self, user_id):
        self.name=""
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


print('原始', '-' * 50)
users = [User(19), User(17), User(18)]
print(users)

print('排序1,key=lambda ui:ui.user_id', '-' * 50)
order_users = sorted(users, key=lambda ui: ui.user_id)  # 根据user_id升序
print(order_users)

print('排序2,key=lambda ui:ui.user_id,reverse=True', '-' * 50)
order_users2 = sorted(users, key=lambda ui: ui.user_id, reverse=True)  # 根据user_id降序
print(order_users2)

print('排序3,key=attrgetter(\'user_id\')', '-' * 50)

from operator import attrgetter
# 根据attrgetter获得迭代对象的属性user_id进行排序
order_users3 = sorted(users, key=attrgetter('user_id'))
print(order_users3)