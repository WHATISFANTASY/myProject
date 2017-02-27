#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# client_tcp.py
import socket

obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
obj.connect(('127.0.0.1', 2222,))  # 连接
print("等待接收服务器数据中...")
ret_bytes = obj.recv(1024)  # 阻塞，如果接收不到消息就等着
print("接收到数据!")

while True:
    inp = input('>').strip()
    if inp == 'q':
        break
    elif inp == '':
        continue
    else:
        obj.sendall(bytes(inp, encoding='utf-8'))  # 向服务器发送指令

        ret_str_size = str(obj.recv(1024), encoding='utf-8')  # 要接受数据的总大小

        print("数据大小为：", ret_str_size)
        ret_str_sum = 0
        while ret_str_size != str(ret_str_sum):
            ret_str_sum += len(obj.recv(1024))
            print(ret_str_sum)





            # print(ret_str)
obj.close()
