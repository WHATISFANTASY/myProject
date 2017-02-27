#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 自定义MyThread模块

import threading
from time import ctime


class MyThread(threading.Thread):
    def __init__(self, func, args, name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getReault(self):
        return self.res

    def run(self):
        print('starting', self.name, 'at:', ctime())
        self.res = self.func(*self.args)
        print(self.name, 'finished at:', ctime())
