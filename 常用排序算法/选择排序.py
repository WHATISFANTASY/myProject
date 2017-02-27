#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import itertools

data_set = [9, 1, 22, 31, -7, 45, 3, 6, 2, 11]

for j in range(len(data_set)):
    min_index = j
    for i in range(j, len(data_set)):
        if data_set[i] < data_set[min_index]:
            min_index = i
    data_set[min_index], data_set[j] = data_set[j], data_set[min_index]

print(data_set)

