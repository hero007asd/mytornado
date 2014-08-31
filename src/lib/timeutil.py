# -*- coding: utf-8 -*-
# @Date    : 2014-08-29 14:23:30
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import time

def get_now_timestamp():
    return int(time.time())

def get_local_datetime(split='-'):
    dt = ['%Y', split, '%m', split, '%d', ' %H:%M:%S']
    datestr = ''.join(dt)
    return time.strftime(datestr, time.localtime())

def get_local_date(split='-'):
    dt = ['%Y', split, '%m', split, '%d']
    datestr = ''.join(dt)
    return time.strftime(datestr, time.localtime())

def str_to_timestamp(strtime, split='-', yearlen=4, hassec=True):
    strarr = ['%Y', split, '%m', split, '%d', ' %H:%M']
    if yearlen == 2:
        strarr[0] = '%y'
    if hassec == True:
        strarr.append(':%S')
    timestr = ''.join(strarr)
    try:
        timeArray = time.strptime(str(strtime), timestr)
    except Exception, e:
        return -1
    
    return int(time.mktime(timeArray))

# print str_to_timestamp('2014-08-14 14:14:14', hassec=False)