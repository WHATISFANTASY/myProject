#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# server_tcp.py
import socket
import os

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(('127.0.0.1', 2222,))
sk.listen(5)
# 接受客户端的请求
while True:
    print('等待连接...')
    conn, address = sk.accept()  # 会阻塞,接受客户端的connect
    conn.sendall(bytes('欢迎致电XXX', encoding='utf-8'))
    while True:
        ret_bytes = conn.recv(1024)
        if not ret_bytes:
            break
            #
            # if ret_str == 'q':
            #     break
            # ret_str
            # conn.sendall(bytes(ret_str + '好', encoding='utf-8'))
        ret_str = str(ret_bytes, encoding='utf-8')
        if ret_str == 'q':
            break

        cmd_result = os.popen(ret_str).read()

        if cmd_result:
            conn.send(bytes(str(len(cmd_result.encode())), encoding='utf-8'))  # 发送数据大小

            conn.send(bytes(cmd_result, encoding='utf-8'))  # 发送数据
        else:
            conn.sendall(bytes('command not found', encoding='utf-8'))


