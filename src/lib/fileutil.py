#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2014-06-19 23:21:22
# @Author  : shitao.tommy (hero007asd@gmail.com)
# @Link    : http://example.org
# @Version : $Id$

import os, fnmatch

def all_files(root, patterns='*', single_level=False, yield_folders=False):
    '''get all files from some folder'''
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pattern in patterns:
                if fnmatch.fnmatch(name, pattern):
                    yield name
                    # yield os.path.join(path, name)
                    break
        if single_level:
            break


#test
if __name__=='__main__':
    for i in all_files(os.getcwd(), patterns='*.py'):
        print i