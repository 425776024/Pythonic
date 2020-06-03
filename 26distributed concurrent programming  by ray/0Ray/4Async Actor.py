#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/8 10:36
# @Author  : xinfa.jiang
# @Site    : 
# @File    : 4Async Actor.py
# @Software: PyCharm

import asyncio
import ray

ray.init()


@ray.remote
class AsyncActor:
    async def run_task(self):
        print("started")
        await asyncio.sleep(1)  # Network, I/O task here
        print("ended")


actor = AsyncActor.remote()
# All 50 tasks should start at once. After 1 second they should all finish.
# they should finish at the same time
ray.get([actor.run_task.remote() for _ in range(50)])
