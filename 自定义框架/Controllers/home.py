#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from wsgiref.simple_server import make_server
import time
from jinja2 import Template
from url import url_dict



def index():
    data = open('Views/index.html').read()
    current_time = str(time.time())

    # 模板渲染
    template = Template(data)
    result = template.render(name='Morra', age='123', current_time=current_time)
    return result.encode('utf-8')


def morra():
    data = open('Views/morra.html').read()
    return data
