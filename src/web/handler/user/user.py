#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-21 23:55:34
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

# from lib.route import route
from lib.tornado_routes import route
from web.handler import BaseHandler

@route(r'/user/index.doc', name='user_index')
class IndexHandler(BaseHandler):
    def get(self):
        self.write('a')
