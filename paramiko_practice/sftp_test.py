#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import paramiko

transport = paramiko.Transport(('192.168.1.96', 22))

transport.connect(username='morra', password='357447218')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('123.py', '/tmp/test.py')  # 将123.py 上传至服务器 /tmp下并改名为test.py

sftp.get('remove_path', 'local_path')  # 将remove_path 下载到本地 local_path

transport.close()
