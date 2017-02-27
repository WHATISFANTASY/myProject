#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import threading
import time


def run(n):
    lock.acquire()  #获取锁
    global num
    num += 1
    lock.release()

lock = threading.Lock()
num = 0
t_obj = []  # 线程实例

for i in range(20000):
    t = threading.Thread(target=run, args=("t-%s" % i,))
    t.start()
    t_obj.append(t)

for t in t_obj:
    t.join()

print "num:", num
