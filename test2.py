#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',8000))
s.listen(5)

while True:
    conn ,add = s.accept()
    conn.sendall(bytes("hello everyone",encoding="utf-8"))

    while True:
        ret_bytes = conn.recv(1024)
        ret_str =  str(ret_bytes,encoding="utf-8")

        if ret_str == 'q':
            break

