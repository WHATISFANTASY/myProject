#!/usr/bin/env python3
# -*- coding:utf-8 -*-




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("s1.html", npm="nohaonpm", haha=INPUTS_LIST)