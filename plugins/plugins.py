#coding=utf-8
import sys
sys.path.append("plugins")
from axis import axis
from glassfish import glassfish
class plugins(object):
    def __init__(self,url,options):
        self.url=url
        self.options=options
    def run(self):
        axis(self.url)
        glassfish(self.url)
        #others


