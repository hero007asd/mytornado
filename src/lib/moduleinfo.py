# -*- coding: utf-8 -*-
# @Date    : 2014-08-21 12:37:59
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

def get_module_doc(module, clazz):
    '''get doc from module
    '''
    modules = get_module(module)
    print modules

    for member in dir(modules):
        member = getattr(modules, member)
        if isinstance(member, type) and issubclass(member, clazz):
            print member.__doc__
            # pass

def get_module(module):
    '''get module by module's str
    '''
    def load_module(m):
        m = m.split('.')
        ms, m = '.'.join(m), m[-1]
        m = __import__(ms, fromlist=[m], level=0)
        return m

    if isinstance(module, (str, unicode)):
        module = load_module(module)
        return module
    raise TypeError('module name should be str, unicode, or byte')

