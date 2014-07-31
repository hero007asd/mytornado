#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-16 18:01:18
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import tornado
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print 'hello world'
        self.write("Hello, world!!!")

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        print 'hello my handler'
# TODO
application = tornado.web.Application([
    (r'/',MainHandler),
    (r'/myhandler', MyHandler),
    ])

if __name__ == "__main__":
    application.listen(8888)
    print 'a'
    tornado.ioloop.IOLoop.instance().start()