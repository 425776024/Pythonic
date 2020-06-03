#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 4:31 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : threadpool  线程池.py
# @Software: PyCharm

import threadpool


def hello(m, n, o):
    print("m = %s, n = %s, o = %s" % (m, n, o))


if __name__ == '__main__':
    # 方法1
    lst_vars_1 = ['1', '2', '3']
    lst_vars_2 = ['4', '5', '6']
    func_var1 = [(lst_vars_1, None), (lst_vars_2, None)]
    # 方法2
    dict_vars_1 = {'m': '1', 'n': '2', 'o': '3'}
    dict_vars_2 = {'m': '4', 'n': '5', 'o': '6'}
    func_var2 = [(None, dict_vars_1), (None, dict_vars_2)]

    pool = threadpool.ThreadPool(3)
    # 参数必须是包含2个元素的元组，第一个解析list，第二个解析dict
    # (*request.args, **request.kwds)
    requests = threadpool.makeRequests(hello, func_var2)
    [pool.putRequest(req) for req in requests]
    pool.wait()

