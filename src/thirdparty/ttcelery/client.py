# -*- coding: utf-8 -*-
# @Date    : 2014-08-26 16:31:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from ttcelery import add

def get_async_result():
    return add.delay(4,4)

def get_processing():
    return get_async_result.ready()

def get_sync_result():
    return get_async_result.get(timeout=1)

# def 