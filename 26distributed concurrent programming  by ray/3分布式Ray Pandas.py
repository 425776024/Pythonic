#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/7 17:28
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 2分布式Ray Pandas.py
# @Software: PyCharm


'''

In Modin, you can start a custom environment in Dask or Ray
and Modin will connect to that environment automatically.
For example, if you'd like to limit the amount of resources that Modin uses,
 you can start a Dask Client or Initialize Ray and Modin will use those instances.
 Make sure you've set the correct environment variable so Modin knows which engine to connect to!
'''

# ps:pip install "modin[all]"
# For Ray:
import os

os.environ["MODIN_ENGINE"] = "ray"  # Modin will use Ray
# os.environ["MODIN_ENGINE"] = "dask"  # Modin will use Dask

import ray

ray.init(plasma_directory="/path/to/custom/dir", object_store_memory=10 ** 10)
# Modin will connect to the existing Ray environment
import modin.pandas as pd
import numpy as np

frame_data = np.random.randint(0, 100, size=(2 ** 10, 2 ** 8))
df = pd.DataFrame(frame_data)
