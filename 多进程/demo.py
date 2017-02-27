#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import time


def f(name):
    time.sleep(2)
    print('hello', name)


if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()

> 转载自 https: // github.com / phodal / awesome - growth


