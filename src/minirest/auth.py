#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-18 16:23:29
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import hashlib
import json

# __ALL__ = ()

def validate_key(key):
    if key != '':
        #TODO get key from db to compare
        return True, _beatiful_json_dumps({'status':0, 'message':'ok'})
    return False, _beatiful_json_dumps({'status': -1, 'message':"key is not validate"})

def validate_signature(key, param, timestamp, signature):
    #TODO if is signature out of date
    if  signature=='' :
        rtmsg = _beatiful_json_dumps({'status': -1, 'message':"signature can not be null"})
        return False, rtmsg
    else:
        sig  = hashlib.md5(param).hexdigest()
        print sig
        if(signature != sig):
            rtmsg = _beatiful_json_dumps({'status': -1, 'message':"validate signature fail"})
            return False, rtmsg
    return True,  _beatiful_json_dumps({'status':0, 'message':'ok'})

def validate_ip(ip):
    #TODO charge ip is ok
    return True,  _beatiful_json_dumps({'status':0, 'message':'ok'})

def validate_method(method):
    pass

def _beatiful_json_dumps(obj):
    return json.dumps(obj, sort_keys=True, indent=4, separators=(',', ':'))