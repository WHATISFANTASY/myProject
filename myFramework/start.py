#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from wsgiref.simple_server import make_server

from myFramework.urls import URLS


def RunServer(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    url = environ['PATH_INFO']

    if url in URLS.keys():
        return URLS[url]()
    else:
        return ['404 not found'.encode('utf-8')]


if __name__ == "__main__":
    httpd = make_server('', 8000, RunServer)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()
