#!/usr/bin/env python3
# -*- coding:utf-8 -*-

with open('db', 'r') as f:
    ret1 = f.readline()
    print(ret1)  # 123
    ret2 = f.readline()
    print(ret2)  # 123

    f.seek(0)
    ret3 = f.readlines()
    print(ret3)

