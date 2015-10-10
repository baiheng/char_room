#!/usr/bin/env python
#coding:utf-8

import tornado.web
import os

import mylog
import conf
from handler import main_handler

setting = dict(
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    autoreload = True,
    )

application = tornado.web.Application(
    handlers = [
        ("/tornado", main_handler.MainHandler),
    ],
    **setting)
