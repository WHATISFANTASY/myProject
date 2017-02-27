#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import socketserver

class FtpServer(socketserver.BaseRequestHandler):
    def handle(self):
        print(self.client_address)



# t = socketserver.ThreadingTCPServer(('127.0.0.1', 9999), FtpServer)