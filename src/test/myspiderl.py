#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-07-01 21:42:00
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib2
from random import choice

URL = 'http://s.taobao.com/search?spm=a230r.1.8.3.jQX5a7&promote=0&sort=sale-desc&initiative_id=staobaoz_20140704&tab=all&q=mac%C3%D4%C4%E3diy%D6%F7%BB%FA&suggest=0_1&stats_click=search_radio_all%253A1#J_relative'
ip_list = {}
ip = '61.155.169.11'
PORT = '808'

#TODO get http://ip:port
#TODO get 

def myproxy():
    proxydict = {}
    proxydict['http'] = 'http://%s:%s' % (ip, PORT)
    print proxydict
    porxy_handler = urllib2.ProxyHandler(proxydict)
    opener = urllib2.build_opener(porxy_handler)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    return opener.open(URL).read()

a = myproxy()
print a.decode('gbk').encode('utf-8')
# if isinstance(a , unicode):
#     print 'a'
#     print a.encode('utf-8')
# else:
#     print 'b'
#     print a.encode('utf-8')
# print len(myproxy())
# fp = open('taobao.txt', 'w')
# fp.write(a)