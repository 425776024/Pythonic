#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 我们可以控制类必须有文档
class Mymeta(type):
    # 只有继承了type类才能称之为一个元类，否则就是一个普通的自定义类
    def __init__(self, class_name, class_bases, class_dic):
        if class_dic.get('__doc__') is None or len(
                class_dic.get('__doc__').strip()) == 0:
            raise TypeError('类中必须有文档注释，并且文档注释不能为空')
        if not class_name.istitle():
            raise TypeError('类名首字母必须大写')
        super(Mymeta, self).__init__(class_name, class_bases,
                                     class_dic)  # 重用父类的功能


try:
    class People(object, metaclass=Mymeta):
        country = 'China'

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def eat(self):
            print('%s is eating' % self.name)

except Exception as e:
    print(e)

try:
    class people(object, metaclass=Mymeta):
        '''
        有注释了！但是，是类小写
        '''
        country = 'China'

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def eat(self):
            print('%s is eating' % self.name)
except Exception as e:
    print(e)
