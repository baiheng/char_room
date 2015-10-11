#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.websocket
from tornado.escape import utf8
import json

import web_handler
import mylog
import utility


class ChatWebSocket(tornado.websocket.WebSocketHandler):
    User = set()
    def prepare(self):
        mylog.logger.debug("ws do prepare")

    def open(self):
        self.set_nodelay(True)
        mylog.logger.debug("add ws user id %s" % id(self))
        ChatWebSocket.User.add(self)
        self.write_message("<p>%s: %s</p>" % (id(self), "欢迎加入聊天室"))

    def on_close(self):
        mylog.logger.debug("remove ws user id %s" % id(self))
        ChatWebSocket.User.remove(self)

    def on_message(self, msg):
        mylog.logger.debug("ws receive msg from user id: %s msg: %s" % 
                (id(self), msg))
        if msg == u"在线的用户数":
            self.write_message("<p>在线的用户数: %s</p>" % 
                    len(ChatWebSocket.User))
            return
        for i in ChatWebSocket.User:
            if i is not self:
                i.write_message("<p>%s: %s</p>" % (id(self), msg))




