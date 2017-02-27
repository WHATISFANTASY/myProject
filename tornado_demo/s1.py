#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import time

import uimethod as mt
import uimodule as md

INPUTS_LIST = []


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('xxx', None)  # 缺省值为None
        if name:
            INPUTS_LIST.append(name)
        self.render("s1.html", npm="nohaonpm", haha=INPUTS_LIST)


class ManagerHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        co = self.get_cookie('auth')
        if co == '1':
            self.render("manager.html")
        else:
            self.redirect("/login")


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html", status_text="")

    def post(self, *args, **kwargs):
        check = self.get_argument("auto", None)
        usr = self.get_argument("username", None)
        pwd = self.get_argument("password", None)

        if usr == "morra" and pwd == "123":
            if check:
                self.set_cookie('auth', '1', expires_days=7)
            else:
                r = time.time() + 10
                self.set_cookie('auth', '1', expires=r)
            self.redirect("/manager")
        else:
            self.render("login.html", status_text="失败")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie('auth', '0')
        self.redirect("/login")


settings = {
    "template_path": "template",  # 模版文件配置
    "static_path": "static",  # 静态文件配置
    "static_url_prefix": "/sss/",  # 静态文件路径前缀配
    'ui_methods': mt,
    'ui_modules': md,
    }

# 路由系统
application = tornado.web.Application([
    (r"/index", MainHandler),
    (r"/login", LoginHandler),
    (r"/manager", ManagerHandler),
    (r"/logout", LogoutHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
