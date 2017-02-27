#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import sys

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
# print(BASE_DIR)
sys.path.append(BASE_DIR)


import threading_socket_server



class ArgvHandler(object):
    def __init__(self, args):
        self.args = args
        print(self.args)
        self.argv_parser()

    def argv_parser(self):  # 解析参数
        if len(self.args) == 1:  # 没有参数，长度为1
            self.help_msg()
        else:
            if hasattr(self, self.args[1]):
                func = getattr(self, self.args[1])
                func()
            else:
                self.help_msg()

    def start(self):
        server = threading_socket_server.ThreadingTCPServer(('0.0.0.0', 9999), threading_socket_server.FtpServer)
        server.serve_forever()

    def stop(self):
        pass

    def help_msg(self):
        msg = '''

        start : start ftp server
        stop : stop ftp server
        create_account : create ftp user account
        help : print help msg

        '''
        sys.exit(msg)
