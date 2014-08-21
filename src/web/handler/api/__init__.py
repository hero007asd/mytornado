#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-18 15:31:46
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

from tornado.web import RequestHandler
from minirest import auth

class BaseApiHandler(RequestHandler):

    def prepare(self):
        #validate key
        key = self.get_argument('key', default='')
        keyOk, keyMsg = auth.validate_key(key)
        if keyOk == False:
            self.write(keyMsg)
            self.finish()
        else:
            #validate ip
            ipOk, ipMsg = auth.validate_ip(self.request.remote_ip)
            if ipOk == False:
                self.write(ipMsg)
                self.finish()
            else:
                #validate signature
                args = self.request.query.split('&')
                signature = self.get_argument('signature', default='')
                timestamp = self.get_argument('timestamp', default='')
                for arg in args:
                    if arg.startswith('signature'):
                        args.pop(args.index(arg))
                params = '&'.join(args)
                signatureOk, signatureMsg = auth.validate_signature(key, params, timestamp, signature)
                if signatureOk == False:
                    self.write(signatureMsg)
                    self.finish()

    def on_finish(self):
        print 'end'
        print self.request.remote_ip

        # print self.request.uri
        # print self.request.remote_ip
        # print self.request.query

    def get_current_user(self):
        pass