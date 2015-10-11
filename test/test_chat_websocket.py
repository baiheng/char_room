#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.websocket
import tornado.testing
from tornado.escape import utf8
from tornado.test.util import unittest

class MyTestCase(tornado.testing.AsyncTestCase):
    @tornado.testing.gen_test
    def test_join_chat_room(self):
        req = tornado.httpclient.HTTPRequest(
                url = "ws://127.0.0.1:8088/chat_websocket"
                )
        conn = yield tornado.websocket.websocket_connect(req)
        msg = yield conn.read_message()
        self.assertIn(u"欢迎加入聊天室", msg)

    @tornado.testing.gen_test
    def test_leave_chat_room(self):
        req = tornado.httpclient.HTTPRequest(
                url = "ws://127.0.0.1:8088/chat_websocket"
                )
        conn = yield tornado.websocket.websocket_connect(req)
        conn.close()

    @tornado.testing.gen_test
    def test_send_receive_msg(self):
        num = 5
        req = tornado.httpclient.HTTPRequest(
                url = "ws://127.0.0.1:8088/chat_websocket"
                )
        conn_list = list()
        for i in xrange(num):
            conn = yield tornado.websocket.websocket_connect(req)
            msg = yield conn.read_message()
            self.assertIn(u"欢迎加入聊天室", msg)
            conn_list.append(conn)
        for i in xrange(num):
            send_msg = u"test %s" % i
            conn_list[i].write_message(send_msg)
            for j in xrange(num):
                if j != i:
                    msg = yield conn_list[j].read_message()
                    self.assertIn(send_msg, msg)

    @tornado.testing.gen_test
    def test_online_user_num(self):
        num = 5
        req = tornado.httpclient.HTTPRequest(
                url = "ws://127.0.0.1:8088/chat_websocket"
                )
        send_msg = u"在线的用户数"
        for i in xrange(num):
            conn = yield tornado.websocket.websocket_connect(req)
            msg = yield conn.read_message()
            self.assertIn(u"欢迎加入聊天室", msg)
            conn.write_message(send_msg)
            msg = yield conn.read_message()
            self.assertIn(u"%s" % (i+1), msg)

