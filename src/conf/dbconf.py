#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-24 22:38:56
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

from lib.database import *
# import settings
# from lib.util import setting_from_object
# from peewee import *

# conf_settings = setting_from_object(settings)

if False:
    db = BaseDb({'db':'md.db'})
else :
    # mysql_db = MysqlDb({'db':conf_settings['db_name'], 'host':conf_settings['db_host'], 'port':conf_settings['db_port'], \
    #                'user':conf_settings['db_user'], 'passwd':conf_settings['db_passwd'], 'charset':'utf8'})
    db = MysqlDb({'db':'diaocha', 'host':'192.168.8.65', 'port': 3306, 'user':'root', 'passwd':'honest1101', 'charset':'utf8'})

    # db2 = Db({'db':conf_settings['db_name'], 'host':conf_settings['db_host'], 'port':conf_settings['db_port'], \
    #                'user':conf_settings['db_user'], 'passwd':conf_settings['db_passwd'], 'charset':'utf8'})
