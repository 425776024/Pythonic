#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 13:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1start.py
# @Software: PyCharm

'''
mmap是一种虚拟内存映射文件的方法，即可以将一个文件或者其它对象映射到进程的地址空间，
实现文件磁盘地址和进程虚拟地址空间中一段虚拟地址的一一对映关系。

普通文件被映射到虚拟地址空间后，程序可以像操作内存一样操作文件，可以提高访问效率，适合处理超大文件
'''

import mmap

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write('Hello Python!\n'.encode())
    f.write('Hello 123!\n'.encode())

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())
    # read content via slice notation
    print(mm[:5])
    # update content using slice notation;
    # note that new content must have same size
    mm[6:14] = " world!\n".encode()
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())
    print(mm.readline())
    # close the map
    mm.close()
