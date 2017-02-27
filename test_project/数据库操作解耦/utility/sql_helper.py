#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pymysql

from 数据库操作解耦 import conf


class MySqlHelper(object):
    def __init__(self):
        self.__conn_dict = conf.conn_dict  # 把数据库连接信心提取到conf中

    def getDict(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data

    def getOne(self, sql, params):
        conn = pymysql.connect(**self.__conn_dict)  # 加**后表示传入的是字典里的数据，否则报错
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        return data
