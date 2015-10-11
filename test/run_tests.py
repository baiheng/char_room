#!/bin/env python
# -*- coding:utf8 -*-

import tornado.testing
from tornado.test.util import unittest

TEST_MODULES = [
        'test_chat_websocket.MyTestCase',
        ]

def all():
    return unittest.defaultTestLoader.loadTestsFromNames(TEST_MODULES)

if __name__ == "__main__":
    tornado.testing.main()
