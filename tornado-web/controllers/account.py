#!/usr/bin/env python3
# -*- coding:utf-8 -*-







class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("login.html")


class LogoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/login")


