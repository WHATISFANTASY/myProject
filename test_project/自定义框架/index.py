#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# py2.7

from wsgiref.simple_server import make_server
import time
from jinja2 import Template
from url import url_dict




# WSGI
def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    # 路由系统
    request_url = environ['PATH_INFO']
    print request_url

    if request_url in url_dict:
        return url_dict[request_url]()
    else:
        return '404'


if __name__ == '__main__':
    httpd = make_server('', 8002, RunServer)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()
