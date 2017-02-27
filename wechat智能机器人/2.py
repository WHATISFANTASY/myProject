#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import itchat

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return msg['Text']

itchat.auto_login()
itchat.run()