#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# p = (4, 5)
# x, y = p
# print(x, y) # 4 5
#
# l = ['Morra', 50, (2012, 1, 1)]
# name, age, _ = l
# print(name, age, _)  # Morra 50 (2012, 1, 1)
#
# l = ['Morra', 20, '123', '456']
# name, age, *num = l
# print(name, age, num)  # Morra 20 ['123', '456']


#
# # 堆栈
# import heapq
# nums = [-4, 1, -12, 3, 4, 5, -50, 43, 4]
# heapq.heapify(nums)
# print(nums)
#
#
# from collections import  OrderedDict
#
# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 2
# d['spam'] = 3
# d['grok'] = 4
#
#
# a= [0,0,0]
# print(hash(a))   #报错
#
# a = {1:2,'c':9}
# print(hash(a))    #报错
#
# a = {1,2,3 }
# print(hash(a))  #报错
#
#
#
# a = (1,2,3)
# print(hash(a))  #2528502973977326415
#
#
# a = 'hello'
# print(hash(a))  #6161994635358828407
#
# class A():
#     pass
# a = A()
# print(hash(a))  #-9223372036584146793


a = [0, 1, 2, 3, 4, 5, 6, 7, 8]
tmp = slice(2, 6, 2)  # 这个是一个slice对象
print(tmp.start)
print(tmp.stop)
print(tmp.step)
print(a[tmp])  #[2,4]
