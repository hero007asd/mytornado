#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-24 23:16:41
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

from conf.dbconf import db
from peewee import *

class Proxy_proxy(db.Model):
    '''Proxy web site Model

    Filed's parameter sample:

    fip = CharField(null=True,
                    index=False,
                    unique=False,
                    verbose_name=None,
                    help_text=None,
                    db_column=None, default=None, choices=None, primary_key=True, *args, **kwargs)
    '''
    fip = CharField(null=True,verbose_name='代理ip',)
    fhost = CharField(null=True,verbose_name='代理host',)
    fport = CharField(null=True,verbose_name='代理port',)
    fprotocal = CharField(null=True,verbose_name='代理协议',)
    ftime = DateTimeField(null=True,verbose_name='验证时间',)
    fcreatetime = IntegerField(null=True, verbose_name='创建时间')

