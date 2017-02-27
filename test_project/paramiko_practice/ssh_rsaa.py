#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import paramiko

private_key = paramiko.RSAKey.from_private_key_file('id_rsa96')   #使用目标的私钥来登录

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect(hostname='192.168.1.96',port=22,username='morra',pkey=private_key)


cmd = 'ps'
stdin, stdout, stderr = ssh.exec_command(cmd)

result = stdout.read()

if not result:
    result = stderr.read()
ssh.close()

print(result.decode())
