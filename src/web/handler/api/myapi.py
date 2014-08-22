#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-22 01:14:23
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os
from web.handler.api import BaseApiHandler
from lib.tornado_routes import route
from tornado import gen

head_title = '登陆接口'

@route(r'api/myapi',name='apitest2')
class TestApi1(BaseApiHandler):
    '''
    @title 测试用的登陆接口
    @method get
    @param username 姓名 12位最长
    @param password 密码 md5加密
    @return {return_code:1, message:null}
    @returnfield status 登陆状态 1.登陆成功2.登陆失败
    @description test api for description
    '''
    @gen.coroutine
    def get(self):
        self.write('a')
