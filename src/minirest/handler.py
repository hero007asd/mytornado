#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-08-19 23:08:12
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$  

import os                                                                                                                                       
from tornado.web import RequestHandler
from tornado import web, template
from web.handler.api import BaseApiHandler
from lib import moduleinfo
import renderhtml

class ApidocHandler(RequestHandler):
    def get(self, apiname):
        # moduleinfo.get_module_doc('web.handler.api.testapi', RequestHandler)
        # modules = moduleinfo.get_module('web.handler.api.testapi')
        try:
            modules = moduleinfo.get_module('web.handler.api.'+apiname)
        except Exception, e:
            raise Exception('module not found')

        headlist = []
        for ml in os.listdir(os.getcwd() + '/web/handler/api'):
            if ml.endswith('.py') and ml !='__init__.py':
                headdict = {}
                moduletmp = moduleinfo.get_module('web.handler.api.'+ml[:-3])
                if hasattr(moduletmp, 'head_title'):
                    headdict['title'] = moduletmp.head_title
                else:
                    headdict['title'] = ml[:-3]
                headdict['url'] = self.request.uri [:self.request.uri.index(apiname)]+ ml[:-3]
                headlist.append(headdict)

        doclist = []
        infodicts = []
        for member in dir(modules):
            headdict = {}
            member = getattr(modules, member)
            uripath = ''
            # print hasattr(member, 'head_title')
            if hasattr(member, 'route_path'):
                uripath = '/' +member.route_path
            if isinstance(member, type) and issubclass(member, BaseApiHandler) and member!=BaseApiHandler :
                doclist.append(member.__doc__)
                anchor = member.__name__

                infodict = {}
                infodict['field'] = []
                infolist = str(member.__doc__).strip().splitlines()
                for i in infolist:
                    if '@title' in i:
                        infodict['title'] = i.strip()[6:]
                    elif '@description' in i:
                        infodict['desc'] = i.strip()[12:]
                    elif '@method' in i:
                        infodict['method'] = i.strip()[7:]
                    elif '@param' in i:
                        fielddict = {}
                        for f in i.split():
                            if i.split().index(f) == 1:
                                fielddict['fname'] = f
                            elif i.split().index(f) == 2:
                                fielddict['fdesc'] = f
                            elif i.split().index(f) == 3:
                                fielddict['fremark'] = f
                        infodict['field'].append(fielddict)
                    infodict['anchor'] = anchor
                    infodict['url'] = self.request.host + uripath
                infodicts.append(infodict)
        # self.write(template.Template(render_html()).generate(value='a'))
        # self.render(template.Template(render_html()))
        # infodict = {'title':'api接口1', 'desc':'api接口测试用1', 
        # 'anchor':'test', 'field':[{'fname':'param1','fdesc':'商品类型', 'fremark':'sfsa上午速度反馈辣椒'}]
        # ,'method':'get', 'url':'http://www.example.com/',}

        self.write(renderhtml.html_string(headlist, 'api接口1.0', infodicts))



def get_title(i):
    return i