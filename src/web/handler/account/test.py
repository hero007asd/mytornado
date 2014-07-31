

# from time import time 
# t = time() 
# lista=[1,2,3,4,5,6,7,8,9,13,34,53,42,44] 
# listb=[2,4,6,9,23] 
# intersection=[] 
# for i in range (1000000): 
#  for a in lista: 
#      for b in listb: 
#          if a == b: 
#              intersection.append(a) 

             
# from time import time 
from lib.tornado_routes import route
from web.handler import BaseHandler

@route(r'/account/index', name='account_index')
class IndexHandler(BaseHandler):
    def get(self):
        self.write('bvd')