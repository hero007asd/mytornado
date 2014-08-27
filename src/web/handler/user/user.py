#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-21 23:55:34
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

# from lib.route import route
from lib.tornado_routes import route
from web.handler import BaseHandler
from web.model import user as u

@route(r'/user/index.doc', name='user_index')
class IndexHandler(BaseHandler):
    def get(self):
        user = u.User.create(name='shitao')
        info = u.User.get(name='shitao')
        # self.render("test.html")
        self.write(info.name)
