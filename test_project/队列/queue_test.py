#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import queue

q = queue.Queue(maxsize=3)      #maxsize设置该队列的最大数据量为3

q.put(1)  # 在队列中放入数据1

q.put(2)  # 在队列中放入数据2

q.put(2)

q.put(3)    #超过该队列最大数据量，阻塞，直到有其他数据取出为该数据留出位置

print(q.qsize())  # 输出当前队列中的数据量

print(q.get())  # 1，取出数据1
print(q.get())  # 2，取出数据2
print(q.get(block=True,timeout=1))  # 如果队列中没有数据，程序等待
# print(q.get_nowait())  # 如果队列中没有数据，则报异常queue.Empty
