#!/usr/bin/env python3
# -*- coding:utf-8 -*-



import tornado.ioloop
import tornado.web
from controllers import home






settings = {
    "template_path": "template",  # 模版文件配置
    "static_path": "static",  # 静态文件配置
    "static_url_prefix": "/sss/",  # 静态文件路径前缀配
    }

# 路由系统
application = tornado.web.Application([
    (r"/index", home.MainHandler),

], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
