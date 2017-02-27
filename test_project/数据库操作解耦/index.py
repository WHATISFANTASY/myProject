#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from 数据库操作解耦.model.admin import Admin


def main():
    usr = input("username:")
    pwd = input("password:")
    admin = Admin()
    result = admin.CheckValidate(usr, pwd)
    if not result:  # 一般会把简单的逻辑放在上面，复杂的逻辑放下面
        print("登录失败！")
    else:
        print("登陆成功！进入后台管理界面..")


if __name__ == "__main__":
    main()
