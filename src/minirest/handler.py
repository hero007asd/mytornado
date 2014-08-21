#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-19 23:08:12
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   

# import web.handler
import os
from tornado.web import RequestHandler

from tornado import web

class ApidocHandler(RequestHandler):
    def get(self):
        get_handler('web.handler.api.testapi')

def get_handler(module):
    def load_module(m):
        m = m.split('.')
        ms, m = '.'.join(m), m[-1]
        m = __import__(ms, fromlist=[m], level=0)
        return m

    if isinstance(module, (str, unicode)):
        module = load_module(module)
        # print module

    for member in dir(module):
        member = getattr(module, member)
        if isinstance(member, type) and issubclass(member, RequestHandler):
            print member.__doc__
            # pass