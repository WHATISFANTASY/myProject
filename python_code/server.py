#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))  # 监听端口
s.listen(5)  # listen()方法监听端口，传入的参数指定等待连接的最大数量
print('等待连接...')



def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:  # 服务器程序通过一个永久循环来接受来自客户端的连接
    sock, addr = s.accept()  # 接收一个新连接：

    # 创建新线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()  # 启动子线程



