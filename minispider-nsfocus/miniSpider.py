#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 须知
# 所需库文件：BeautifulSoup
# python版本：3.0以上



import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = input("输入网址：")
html = urlopen(url.strip())
bsObj = BeautifulSoup(html.read(), "lxml")

tagObj = bsObj.findAll("table")

list = []

for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        list.append(link.attrs['href'])

with open('urllist.txt', 'w') as f:
    for i in list:
        tmp = re.findall(r'/update/downloads/id/[0-9]+', i)
        if bool(tmp):
            new_url = "http://update.nsfocus.com" + tmp[0] + "\n"
            f.write(new_url)


exit("\n任务完成!")