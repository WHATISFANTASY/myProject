#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import multiprocessing
import time
import os


def info(title):
    print(title)
    print('moudle name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
    print("\n")


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    info('mian process line')  # 主程序进程
    p = multiprocessing.Process(target=f, args=('morra',))
    p.start()
"""
mian process line
moudle name: __main__
parent process: 31732   #这是pycharm的进程号
process id: 19816

"""
