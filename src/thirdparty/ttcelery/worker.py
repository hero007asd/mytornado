# -*- coding: utf-8 -*-
# @Date    : 2014-08-26 16:31:33
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from celery import Celery

app = Celery('tasks', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x+y