#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/1/2 2:41 PM
# @Author  : xinfa.jiang
# @Site    : 
# @File    : pandas多线程.py
# @Software: PyCharm

import numpy as np
import pandas as pd
from multiprocessing import Pool


def parallelize_func(data):
    # 最终对df进行操作的函数
    # 数据
    df = data[0]
    # 额外序号
    i = data[1]
    print(i)
    return df


def parallelize_dataframe(df, func, n_cores=4):
    df_split = np.array_split(df, n_cores)
    data = list(zip(df_split, list(range(n_cores))))
    pool = Pool(n_cores)
    df = pd.concat(pool.map(func, data))
    pool.close()
    pool.join()
    return df

if __name__ == '__main__':
    n_cores = 4
    test_df=parallelize_dataframe(test_df, parallelize_func, n_cores=n_cores)