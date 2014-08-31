# -*- coding: utf-8 -*-

# mydict = [1,2,3,4]
# print 'a' if len(mydict)>4 else []

# class A(object):
#     def __init__(self):
#         self._foo = 100
#     @property
#     def foo(self):
#         return self._foo
#     @foo.setter
#     def foo(self, value):
#         self._foo = value
    
#     @property
#     def a(self):
#         print 'a'

# my = A()
# my.foo = 120
# print my.foo
# 
# import os,glob
# def findfiles(dirname,pattern):
#      cwd = os.getcwd() #保存当前工作目录
#      if dirname:
#          os.chdir(dirname)
  
#      result = []
#      for filename in glob.iglob(pattern): #此处可以用glob.glob(pattern) 返回所有结果
#          result.append(filename)
#      #恢复工作目录
#      os.chdir(cwd)
#      return result
# import os
# print os.getcwd()
# print os.path.dirname(__file__)
# print  findfiles(os.path.join(os.path.dirname(__file__)), '*.py')
# import time
# print time.localtime()
# print time.gmtime()
# # print time.mktime()
# print time.time()
# print int(time.time())