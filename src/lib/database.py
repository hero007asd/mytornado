#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-23 23:13:26
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import peewee
from playhouse.signals import Model as _model


class BaseDb(object):
    
    fn = peewee.fn
    R = peewee.R
    RawQuery = peewee.RawQuery
    DoesNotExist = peewee.DoesNotExist
    
    
    def __init__(self,kw):
        self.config = kw
        self.load_database()
        self.Model = self.get_model_class()
        
    def load_database(self):
        self.db = self.config.pop('db')
        self.database = peewee.SqliteDatabase(self.db, **self.config)
        # self.database = Db.FixMySQLDatabase(self.db, **self.config)
        
    def get_model_class(self):
        class BaseModel(_model):
            class Meta:
                database = self.database
        return BaseModel
                
    def connect(self):
        self.database.connect()
    
    def close(self):
        try:
            self.database.close()
        except:pass

class MysqlDb(BaseDb):
    def __init__(self, kw):
        self.config = kw
        self.load_database();
        self.Model = self.get_model_class()
        # super.__init__(self, kw)

    def load_database(self):
        self.db = self.config.pop('db')
        self.database = peewee.MySQLDatabase(self.db, **self.config)


    def get_model_class(self):
        class BaseModel(_model):
            class Meta:
                database = self.database
                read_slaves = (self.database, )
        return BaseModel