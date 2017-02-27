#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import threading
import multiprocessing
import time


def thread_run():
    print(threading.get_ident())


def run(name):
    time.sleep(2)
    print('hello', name)
    t = threading.Thread(target=thread_run)  # 每个进程又执行一个线程
    t.start()


if __name__ == '__main__':

    for i in range(10):
        p = multiprocessing.Process(target=run, args=("morra %s" % i,))
        p.start()
