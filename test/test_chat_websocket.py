#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import tornado.gen
import tornado.httpclient
import tornado.websocket
import tornado.testing
from tornado.escape import utf8
from tornado.test.util import unittest
import time

class MyTestCase(tornado.testing.AsyncTestCase):
    # 测试登录聊天室功能
    # 成功登录后会返回“欢迎加入聊天室”
    @tornado.testing.gen_test
    def test_join_chat_room(self):
        req = tornado.httpclient.HTTPRequest(
                url = "ws://127.0.0.1:8088/chat_websocket"
                )
        conn = yield tornado.websocket.websocket_connect(req)
        msg = yield conn.read_message()
        self.assertIn(u"欢迎加入聊天室", msg)

    # 测试发送消息与接收消息功能
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

    # 测试在线人数功能
    # 1.新用户登录在线人数会增加
    # 2.用户离开在线人数会减少
    @tornado.testing.gen_test
    def test_online_user_num(self):
        num = 5
        req = tornado.httpclient.HTTPRequest(
                url = "ws://127.0.0.1:8088/chat_websocket"
                )
        send_msg = u"在线的用户数"
        conn_list = list()
        for i in xrange(num):
            conn = yield tornado.websocket.websocket_connect(req)
            msg = yield conn.read_message()
            self.assertIn(u"欢迎加入聊天室", msg)
            conn.write_message(send_msg)
            msg = yield conn.read_message()
            self.assertIn(u"%s" % (i+1), msg)
            conn_list.append(conn)
        for i in xrange(num):
            conn_list[i].write_message(send_msg)
            msg = yield conn_list[i].read_message()
            conn_list[i].close()
            self.assertIn(u"%s" % (num - i), msg)
            time.sleep(0.1)


