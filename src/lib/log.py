# -*- coding: utf-8 -*-
# @Date    : 2014-06-19 23:28:16
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os
import logging
import multiprocesslogging
import settings
# from bootloader

def log_info(handler):
    '''log used in setting's log_function
       for log info
    '''
    log = logging.getLogger(settings.LOG_NAME)
    log.info( '%s  %s  %s  %s' %(handler.get_status(), handler.request.method, handler.request.uri, handler.request.remote_ip))

    #TODO to queue --->db

def log_exception(handler, exc_type, exc_value, exc_traceback):
    '''log used in handler's log_exception
       for log exception
    '''
    log = logging.getLogger(settings.LOG_NAME)
    log.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    #TODO to sentry --- queue --- db

def log_warning(hanlder):
    print 'warning'

def init_log(logger_name):
    log = logging.getLogger(logger_name)
    log.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-s %(asctime)s %(levelname)-s %(filename)-s %(message)-s')
    fileHandler = multiprocesslogging.MultiProcessTimedRotatingFileHandler(settings.LOG_PATH,'midnight',1,0)
    fileHandler.suffix = "%Y%m%d.log"
    fileHandler.setFormatter(formatter)
    log.addHandler(fileHandler)

    return log