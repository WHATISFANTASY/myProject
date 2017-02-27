#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os

print(__file__)
#pycharm中会自动生成绝对路径，但是如果不用IDE就是相对路径，所以需要使用 os.path.abspath
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# print(BASE_DIR)
sys.path.append(BASE_DIR)

# for i in sys.path:
#     print(i)


# from modules import main


print(__file__)


if __name__ == "__main__":
    # EntryPoint = main.ArgvHandler(sys.argv)
    pass