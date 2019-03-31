#coding=utf-8
#Author is Naivete
#github:https://www.github.com/nihaohello
#blog:http://www.youknowi.xin
import sys
import os
import re
import argparse
import traceback
import config
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from plugins import plugins
#80,4848,7001,7002,8000,8001,8080,8081,8888,9999,9043,9080
class MiddlewareScan(object):
    def __init__(self,arg,config):
        self.arg=arg
        self.config=config
    def run(self):
        P = plugins.plugins(self.arg,self.config)
        P.run()
def main():
    arg = argparse.ArgumentParser(description='MiddlewareScan By Naivete')
    arg.add_argument('-u', '--url', help='url site', dest='url')
    arg.add_argument('-i', '--file', help='file name , fill url ', dest='file')
    arg.add_argument('-p', '--options', help='options', dest='options')
    arg.add_argument('-t', '--thread', help='thread num', dest='thread')
    arg = arg.parse_args()
    if len(sys.argv)<=2:
        os.system("python "+sys.argv[0]+" -h")
        exit()
    print("开始检测中间件相关漏洞:")
    if arg.thread:
        config.ThreadNum=arg.thread
    if not arg.options:
        arg.options="all"
    if arg.url:
        if not re.match(r'^https?:/{2}\w.+$', url):
            print("输入标准的url，如:http://www.baidu.com")
            exit()
        try:
            S=MiddlewareScan(arg,config)
            S.run()
        except Exception:
            print(traceback.print_exc())
    if arg.file:
        multiprocessing_list=[]
        f = open(arg.file, encoding="utf-8")
        for url in f.readlines():
            url = url.rstrip("\n")
            arg.url = url
            if not re.match(r'^https?:/{2}\w.+$', url):
                if not url.startswith("http"):
                    arg.url="http://"+url
            S = MiddlewareScan(arg, config)
            multiprocessing_list.append(S.run())
        f.close()
        pool=multiprocessing.Pool(config.Process)
        try:
            #pool.apply_async(multiprocessing_list)
            for i in multiprocessing_list:
                pool.apply_async(i)
            pool.close()
            pool.join()
        except Exception:
            print(traceback.print_exc())
    print("\n\n相关漏洞检测完成。")
if __name__ == '__main__':
    main()