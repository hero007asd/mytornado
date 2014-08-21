#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-15 18:23:39
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

from tornado.web import UIModule

class TestModule(UIModule):
    def render(self):
        return self.render_string('widget/a.html')