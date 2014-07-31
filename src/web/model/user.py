#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-24 23:16:41
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

from conf.dbconf import db
from peewee import *
class User(db.Model):
    name = CharField()


