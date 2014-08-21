#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-18 15:48:48
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os
from web.handler.api import BaseApiHandler
from lib.tornado_routes import route
from tornado import gen
import md5

@route(r'api/test',name='apitest')
class TestApi(BaseApiHandler):
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
        # print self.__doc__.splitlines()
        # print  self.__name__
        # print self.__class__.__name__

class Test1Api(BaseApiHandler):
    '''
    @param username234
    '''
    def get(self):
        print 'asd'