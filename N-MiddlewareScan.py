#coding=utf-8
#Author is Naivete
#github:https://www.github.com/nihaohello
#blog:http://www.youknowi.xin
import sys
import os
import argparse
import traceback
import config
from concurrent.futures import ThreadPoolExecutor
from plugins import plugins
#80,4848,7001,7002,8000,8001,8080,8081,8888,9999,9043,9080
class MiddlewareScan(object):
    def __init__(self,url,options):
        self.url=url
        self.options=options
    def run(self):
        P = plugins.plugins(self.url,self.options)
        P.run()
def main():
    arg = argparse.ArgumentParser(description='MiddlewareScan By Naivete')
    arg.add_argument('-u', '--url', help='url site', dest='url')
    arg.add_argument('-i', '--file', help='file name', dest='file')
    arg.add_argument('-p', '--options', help='options', dest='options')
    arg.add_argument('-t', '--thread', help='thread num', dest='thread')
    arg = arg.parse_args()
    if arg.thread:
        config.ThreadNum=arg.thread
    if not arg.options:
        arg.options="all"
    if arg.url:
        try:
            S=MiddlewareScan(arg.url,arg.options)
            S.run()
        except Exception:
            print(traceback.print_exc())
    if arg.file:
        try:
            with open(arg.file,encoding="utf-8") as f:
                with ThreadPoolExecutor(config.ThreadNum) as excetor:
                    for url in f.readlines():
                        try:
                            url=url.rstrip("\n")
                            S=MiddlewareScan(url,arg.options)
                            excetor.submit(S.run())
                        except Exception:
                            pass
            f.close()
        except Exception:
            print(traceback.print_exc())
    print("相关漏洞检测完成。")
if __name__ == '__main__':
    print("开始检测中间件相关漏洞:")
    main()


