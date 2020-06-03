#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 17:21
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 1Pandas.py
# @Software: PyCharm

import modin.pandas as pd
import numpy as np

frame_data = np.random.randint(0, 100, size=(2 ** 10, 2 ** 8))
df = pd.DataFrame(frame_data)

'''
PS:pip install modin
'''

# 然后像正常的pandas那样操作，这样，你的所有pandas操作都是并发的
# 数据越庞大，效果越明显
stocks_df = pd.read_csv("xx.csv")

'''
To use Modin, you do not need to know how many cores your system has and 
you do not need to specify how to distribute the data. 
In fact, you can continue using your previous pandas notebooks 
while experiencing a considerable speedup from Modin, 
even on a single machine. Once you’ve changed your import statement, 
you’re ready to use Modin just like you would pandas.
'''
