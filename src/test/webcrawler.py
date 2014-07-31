#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-27 22:00:08
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import urllib2
from random import choice

USER = 'foo'
PASSWD = 'bar'
IPLIST = ['114.80.136.112', ]
PORT = '8080'
URL = 'http://www.iot-dc.com/'

ip = choice(IPLIST)
print ip

def myproxy():
    proxydict = {}
    proxydict['http'] = 'http://%s:%s' % (ip, PORT)
    # proxydict['http'] = 'http://%s:%s@%s:%s' % (USER, PASSWD, IP, PORT)
    print proxydict
    porxy_handler = urllib2.ProxyHandler(proxydict)
    # porxy_handler = urllib2.ProxyHandler()
    opener = urllib2.build_opener(porxy_handler)
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    # urllib2.install_opener(opener)
    # sContent = urllib2.urlopen(URL)
    # print sContent.read()
    print opener.open(URL, timeout=40).read()
myproxy()

headerdict = {
    'GET' : URL,
    'HOST' : 'www.iot-dc.com',
    'Referer' : 'http://www.baidu.com',

}

def myproxy1():
    req = urllib2.Request(URL)
    for key in headerdict:
        req.add_header(key, headerdict[key])
    r = urllib2.urlopen(req)
    print r.read()

# myproxy1()

##  __TODO download media files
# TODO download text/plain to database
# TODO multithreading 

url = 'http://www.baidu.com'
# page = urllib2.urlopen(url).readline()
# page = urllib2.urlopen(url).getcode()
# page = urllib2.urlopen(url).info()
# print page.find('baidu')


from urlparse import urlparse, urlsplit
url = 'http://www.baidu.com/abc?a=1'
# parsed = urlparse(url)
# parsed = urlsplit(url)
# print parsed
# print parsed.geturl()

# def multi_open(opener, *arg):
#     while True:
#         retryTimes = 20
#         while retryTimes > 0:
#             try:
#                 return opener.open(*arg)
#             except Exception, e:
#                 print e
#                 retryTimes -= 1




html_escape_table = {
    "&": "&",
    '"': '"',
    "'": "'",
    ">": ">",
    "<": "<",
    u"·":"·",
    u"°":"°",
    #regular expression
    ".":r"\.",
    "^":r"\^",
    "$":r"\$",
    "{":r"\{",
    "}":r"\}",
    "\\":r"\\",
    "|":r"\|",
    "(":r"\(",
    ")":r"\)",
    "+":r"\+",
    "*":r"\*",
    "?":r"\?",
}

def html_escape(text):
    """Produce entities within text."""
    tmp="".join(html_escape_table.get(c,c) for c in text)
    return tmp.encode("utf-8")
