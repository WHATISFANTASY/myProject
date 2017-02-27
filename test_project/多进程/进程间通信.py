#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])


if __name__ == "__main__":
    q = Queue()  # 通过进程Queue来解决进程之间的数据交互
    p = Process(target=f, args=(q,))  # 子进程
    p.start()

    print(q.get())  # [42, None, 'hello']，主进程获取到了子进程数据，先序列化后反序列化