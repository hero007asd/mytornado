#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-19 23:28:16
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import settings
import os
from lib import util
from lib import common_uimodule
from importlib import import_module

settings = util.setting_from_object(settings)

uimodules = []

uimodules.append(common_uimodule)

# set uimodules
for i in os.listdir('web/uiwidget'):
    if i.endswith('.py') and i != '__init__.py':
        module = import_module('.%s' % i[:-3], 'web.uiwidget')
        uimodules.append(module)

settings.update({
        'template_path':os.path.join(os.path.dirname(__file__), 'web/template'),
        'static_path':os.path.join(os.path.dirname(__file__), 'static'),
        'upload_path':os.path.join(os.path.dirname(__file__), 'static/upload'),
        'cookie_secret':"x1g5zGibQISFc0+t2G2qcwraupWIKEt2ibwCmQgSfcU=",
        'login_url':'/signin',
        "xsrf_cookies": True,
        'ui_modules' : uimodules,
        'autoescape':None
    })


