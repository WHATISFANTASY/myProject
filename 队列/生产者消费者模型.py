#!/usr/bin/env python3
#-*- coding:utf-8 -*-


import threading,time
import queue


q = queue.Queue(maxsize=10)

def Producer(name):
    count = 1
    while True:
        q.put("包子%s" %count)
        print("生产了包子")
        count+=1
        time.sleep(2)

def Consumer(name):
    while True:
        print("[%s] 取到 [%s] 并吃了它..."%(name,q.get()))
        time.sleep(1)
p = threading.Thread(target=Producer,args=("morra",))
c1 = threading.Thread(target=Consumer,args=("jack",))
c2 = threading.Thread(target=Consumer,args=("tommy",))


p.start()
c1.start()
c2.start()