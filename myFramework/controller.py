#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
from jinja2 import Template


def index():
    with open(os.path.join("views", "index.html"), "r") as f:
        data = f.read()

    data = Template(data).render(name="Morra", user_list=["a", "b", "c"])

    ret = [data.encode('utf-8')]
    return ret


def new():
    with open(os.path.join("views", "new.html"), "r") as f:
        data = f.read()

    ret = [data.encode('utf-8')]
    return ret
