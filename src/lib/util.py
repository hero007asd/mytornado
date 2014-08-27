#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-19 23:21:22
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$
import os, glob
import re
import urllib
# import simplejson

def setting_from_object(obj):
    setting = dict()
    for key in dir(obj):
        if key.isupper():
            setting[key.lower()] = getattr(obj, key)
    return setting

def findfiles(dirname,pattern):
     cwd = os.getcwd() #保存当前工作目录
     if dirname:
         os.chdir(dirname)
  
     result = []
     for filename in glob.iglob(pattern): #此处可以用glob.glob(pattern) 返回所有结果
         result.append(filename)
     #恢复工作目录
     os.chdir(cwd)
     return result

def generate_secretkey():
    import base64
    import uuid
    return base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)


def find_subclasses(klass, include_self=False):
    accum = []
    for child in klass.__subclasses__():
        accum.extend(find_subclasses(child, True))
    if include_self:
        accum.append(klass)
    return accum

def vmobile(mobile):
    return re.match(r"((13|14|15|18)\d{9}$)|(\w+[@]\w+[.]\w+)", mobile)

# def sendmsg(settings, mobile, content):
#     url = "%s?accesskey=%s&secretkey=%s&mobile=%s&content=%s" % (settings['sms_gateway'], settings['sms_key'], settings['sms_secret'], mobile, urllib.quote_plus(content))
#     result = simplejson.loads(urllib.urlopen(url).read())
    
#     if int(result['result']) > 1:
#         raise Exception('无法发送')
