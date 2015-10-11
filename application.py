#!/usr/bin/env python
#coding:utf-8

import tornado.web
import os

import mylog
from handler import chat_websocket

setting = dict(
    template_path = os.path.join(os.path.dirname(__file__),"template"),
    static_path = os.path.join(os.path.dirname(__file__), "static"),
    autoreload = True,
    )

application = tornado.web.Application(
    handlers = [
        ("/chat_websocket", chat_websocket.ChatWebSocket),
    ],
    **setting)
