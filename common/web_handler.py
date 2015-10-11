#!/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import traceback
from tornado.escape import utf8

import mylog

class WebHandler(tornado.web.RequestHandler):
    def initialize(self):
        mylog.logger.debug("query headers: %s" % self.request.headers)
        mylog.logger.debug("query cookies: %s" % self.request.cookies)
        mylog.logger.debug("query input: %s" % self.request.query_arguments)
        mylog.logger.debug("body input: %s" % self.request.body)

    def on_finish(self):
        mylog.stat_logger.info("(%s), (%s), (%s), (%s), (%s), (%s)" %
                (self.get_status(), self.request.remote_ip, 
                    self.request.headers['X-Real-Ip'],
                    (self.request.request_time()*1000), 
                    self.request.full_url(), self.request.method))

    def write_error(self, status_code, **kwargs):
        self.set_header('Content-Type', 'text/plain')
        if "exc_info" in kwargs:
            mylog.logger.error("%s" % "".join(traceback.format_exception(*kwargs["exc_info"])))
        self.finish("500")

    def decode_argument(self, value, name=None):
        try:
            return utf8(value)
        except UnicodeDecodeError:
            raise HTTPError(400, "Invalid unicode in %s: %r" %
                            (name or "url", value[:40]))
