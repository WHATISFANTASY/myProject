#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from 数据库操作解耦.utility import MySqlHelper

class Admin():
    def __init__(self):
        self.__helper = MySqlHelper()

    # def getOne(self, id):
    #     sql = "select * from admin where id =%s"
    #     params = (id,)
    #     return self.__helper.getOne(sql, params)

    def CheckValidate(self,username,password):
        sql = "select * from admin where username=%s and password=%s"
        params=(username,password)
        return self.__helper.getOne(sql,params)