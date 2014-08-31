#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-07-02 23:51:24
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

# todo : exception handle\loop to remove what is unavaliable\get last N avaliable data\
# TODO: add gearman || celery || zeromq || rabbitmq
# TODO :  do it 00:00 everyday,after that do crawler EBussiness's data
'''ip proxy's  crawler
'''
import json
import re
import lxml.html as HTML#use xpath replace re
from lxml import etree
import urllib2

proxy_resource_url = 'http://www.xici.net.co/nn/'
proxy_assert_dict = {
    'GET' : proxy_resource_url,
    'HOST' : 'www.xici.net.co',
    'Referer' : 'http://www.baidu.com',
}

def getproxylist():
    req = urllib2.Request(proxy_resource_url)
    for key in proxy_assert_dict:
        req.add_header(key, proxy_assert_dict[key])
    r = urllib2.urlopen(req, timeout=40)
    proxysource = r.read()
    return proxysource

def handle_proxy_list(proxysource):
    tree = etree.HTML(proxysource)
    nodes =  tree.xpath(u'//tr[@*]')

    parentarray = [[]]
    for node in nodes:
        tdnode = node.xpath(u'./td')
        childarray = []
        for childnode in tdnode:
            if childnode.text is not None:
                value = ''
                if isinstance(childnode.text, unicode):
                    value = childnode.text.encode('utf-8')
                elif isinstance(childnode.text, str):
                    value = childnode.text
                childarray.append(value)
        parentarray.append(childarray)
    return parentarray
    # htmlSource = HTML.fromstring(proxysource)
    # print htmlSource
    # a = htmlSource.xpath(u'//table/tbody/tr[3]/td[2]')

from models.crawler import Proxy_proxy
from lib.timeutil import get_now_timestamp, str_to_timestamp
def save_proxylist():
    '''save proxy info list '''
    proxylist = handle_proxy_list(getproxylist())

    # get last time of update
    query = Proxy_proxy.select(Proxy_proxy.ftime).order_by(Proxy_proxy.ftime.desc()).limit(1)
    try:
        lasttime = str_to_timestamp(query[0].ftime)
    except Exception, e:
        lasttime = 0

    for pa in proxylist[::-1]:
        if len(pa) > 0 and str_to_timestamp(pa[-1], yearlen=2, hassec=False) > lasttime:
            proxy = Proxy_proxy()
            proxy.fip = pa[0]
            # proxy.fhost = pa[1]
            proxy.fport = pa[1]
            proxy.fprotocal = pa[4]
            proxy.ftime = pa[-1]
            proxy.fcreatetime = get_now_timestamp()
            proxy.save()
            # proxy.close()

    # flush redis
    


# proxylist = handle_proxy_list(getproxylist())
# print len(proxylist)
# for pa in proxylist:
#     print pa