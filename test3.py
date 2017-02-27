#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os


tmp = os.stat('text.txt').st_size
tmp2 = os.path.basename('text.txt')
tmp3 = os.path.dirname(__file__)
print(tmp)
print(tmp2)
print(tmp3)