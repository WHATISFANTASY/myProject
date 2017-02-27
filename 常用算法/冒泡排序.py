#!/usr/bin/env python3
# -*- coding:utf-8 -*-

data_set = [9, 1, 22, 31, 45, 3, 6, 2, 11]

for j in range(len(data_set)):
    for i in range(len(data_set) - j - 1):
        if data_set[i] > data_set[i + 1]:
            data_set[i], data_set[i + 1] = data_set[i + 1], data_set[i]
print(data_set)



