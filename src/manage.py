#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-17 23:04:35
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import logging
import tornado
import tornado.web
import os
from tornado.httpserver import HTTPServer
from tornado.options import define, parse_command_line, options
from bootloader import settings
# from lib.route import Route
# add handler here
from lib.tornado_routes import make_handlers, get_all_handler
from lib import log
from web import model
from minirest import handler as h

define('cmd', default='runserver', metavar='runserver|syncdb')   # python manage.py --cmd=syncdb
define("port", default=8080, type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                    tornado.web.url(r"/static/(.+)", tornado.web.StaticFileHandler, dict(path=settings['static_path']), name='static_path'),
                    tornado.web.url(r"/upload/(.+)", tornado.web.StaticFileHandler, dict(path=settings['upload_path']), name='upload_path'),
                    ]
        URL_PREFIX = ''
        # handlers += make_handlers(URL_PREFIX, get_all_handler(os.path.dirname(__file__), 'web/handler/'))
        handlers += make_handlers(URL_PREFIX, get_all_handler(os.path.dirname(os.path.abspath(__file__)), 'web/handler/', 'web', 'handler'))
        handlers += [tornado.web.url(r'/apidoc/doc/(.*)', h.ApidocHandler)]  #apidoc handler
        tornado.web.Application.__init__(self, handlers, **settings)

def syncdb():
    from lib.util import find_subclasses
    from conf.dbconf import db
    from web.model.user import User  #TODO auto to get model 

    models = find_subclasses(db.Model)

    for model in models:
        print model
        if model.table_exists():
            model.drop_table()
        model.create_table()
        logging.info('created table:%s' % model._meta.db_table)

def runserver():
    http_server = HTTPServer(Application(), xheaders = True)
    http_server.listen(options.port)
    # http_server.bind(options.port)
    # http_server.start(num_processes=0)

    loop = tornado.ioloop.IOLoop.instance()

    # print 'server running on http://localhost:%d' % (options.port)
    logging.info("Server running  on http://0.0.0.0:%d" %(options.port))
    # sys.excepthook = log.log_exception
    
    loop.start()

if __name__ == '__main__':
    parse_command_line()

    log.init_log(settings['log_name'])
    
    if options.cmd == 'syncdb':
        syncdb()
    else:
        runserver()
