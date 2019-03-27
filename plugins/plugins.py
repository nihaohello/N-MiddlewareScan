#coding=utf-8
import sys
sys.path.append("plugins")
from axis import axis
class plugins(object):
    def __init__(self,url,options):
        self.url=url
        self.options=options
    def run(self):
        axis(self.url)
        #others


