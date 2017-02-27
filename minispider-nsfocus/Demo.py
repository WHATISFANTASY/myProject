#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 未完成，需要进一步学习ajax爬虫的

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import datetime

random.seed(datetime.datetime.now())  # 用系统当前时间生成一个随机数生成器


def getLinks(url):
    linkList = []
    newLinkList = []
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "lxml")
    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            linkList.append(link.attrs['href'])

    for i in linkList:
        tmp = re.findall(r'http://update.nsfocus.com/update/[a-zA-Z]+', i)
        if bool(tmp):
            newLinkList.append(tmp[0])

    return newLinkList


links = getLinks("http://update.nsfocus.com")

randomLink = random.randint(0, len(links) - 1)

print(links[randomLink])





# while len(links) > 0:
#     newAriticle = links[random.randint(0, len(links) - 1)]
#     print(newAriticle)
