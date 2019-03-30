#coding=utf-8
import sys
import requests
import os
import json
import traceback
from concurrent.futures import ThreadPoolExecutor
from plugins.special_plugin_ import special_plugin_
sys.path.append("plugins")
import plugins
current_file=os.path.dirname(os.path.abspath(__file__))
from user_agent import get_user_agent
class plugins(object):
    def __init__(self,arg,config):
        self.arg=arg
        self.config=config
        self.url=arg.url
        self.options=arg.options
        self.ThreadNum=config.ThreadNum
        self.Timeout=config.Timeout
        self.vuln=[]
        self.port=config.port
    def run(self):
        print("\n第一部分standard_poc 测试开始:")
        print("***********************")
        files=os.listdir(current_file)
        list_8080=["axis","glassfish","jboss","resin","spring","tomcat","struts2"]
        with ThreadPoolExecutor(self.ThreadNum) as excetor:
            for file in files:
                if "_plugin.py" in file:
                    module = file.rstrip(".py")
                    pocs = __import__(module).pocs
                    module=module.strip("_plugin")
                    if module in list_8080:
                        self.port=8080
                    if module in ["weblogic"]:
                        self.port=7001
                    excetor.submit(self.check(pocs))
        if self.vuln:
            print("\n\n\n第一部分 standard_poc 测试出的漏洞有：")
            for vuln in self.vuln:
                print(vuln)
        else:
            print("\n\n\n第一部分 standard_poc 没有测试出任何的漏洞。")
        print("\n\n\n第二部分：\n开始测试特定的poc脚本：")
        print("***********************")
        special_plugin_(self.arg,self.config)
    def request_get(self,url,params,data,flags,success_num,success,fail,pocs):
        try:
            headers = get_user_agent()
            s = requests.get(url=url+":"+self.port, params=params, headers=headers,timeout=self.Timeout)
            if not flags:
                if s.status_code!=404:
                    self.vuln.append(self.url+success)
            for flag in flags:
                if flag in s.text:
                    success_num = success_num + 1
            if success_num > 0:
                self.vuln.append(success + " \npocs: \n" + pocs)
                print(success + " \npocs: \n" + pocs)
        except Exception:
            success_num=success_num+1
            if success_num<=2:
                self.request_get(url, params, data, flags, success_num,success,fail,pocs)
    def request_post(self,url,params,data,flag,success_num,username,password,success,fail,pocs):
        try:
            headers = {'User-Agent': get_user_agent()}
            s = requests.post(url=url+":"+self.port, data=data, headers=headers,timeout=self.Timeout)
            for flag in poc["flag"]:
                if flag in s.text:
                    success_num = success_num + 1
            if success_num > 0:
                if pocs["admin_bursk"]==True:
                    self.vuln.append("success url:" + utl + " " + success + ",username:%s password:%s" % (username, password))
                    print("success url:" + utl + " " + success + ",username:%s password:%s" % (username, password))
                else:
                    self.vuln.append(success + " \n pocs: \n" + pocs)
                    print(success + " \n pocs: \n" + pocs)
        except Exception:
            success_num=success_num+1
            if success_num<=2:
                self.request_post(url,params,data,flag,success_num,username,password,success,fail,pocs)
    def check(self,pocs):
        with ThreadPoolExecutor(self.ThreadNum) as excetor:
            for poc in pocs:
                for url in poc["url"]:
                    try:
                        url = self.url + url
                        if poc["requests_option"] == "GET":
                            if not poc["params"]:
                                poc["params"].append("seize")
                            for params in poc["params"]:
                                success_num = 0
                                try:
                                    excetor.submit(self.request_get(url, params, poc["data"], poc["flag"], success_num, poc["success"],poc["fail"],poc))
                                except Exception:
                                    print(traceback.print_exc())
                        if poc["requests_option"] == "POST":
                            if not poc["data"]:
                                poc["data"].append("seize")
                            for data in poc["data"]:
                                try:
                                    if poc["admin_bursk"] == "True":
                                        for username in poc["username"]:
                                            for password in poc["password"]:
                                                success_num = 0
                                                try:
                                                    excetor.submit(self.request_post(url, poc["params"], data, poc["flag"],success_num, username, password, poc["success"],poc["fail"],poc))
                                                except Exception:
                                                    print(traceback.print_exc())
                                except Exception:
                                    print(traceback.print_exc())
                                else:
                                    success_num = 0
                                    try:
                                        for data in poc["data"]:
                                            success_num = 0
                                            try:
                                                excetor.submit(self.request_post(url, poc["params"], data, poc["flag"], success_num,poc["username"], poc["password"], poc["success"],poc["fail"],poc))
                                            except Exception:
                                                print(traceback.print_exc())
                                    except Exception:
                                        print(traceback.print_exc())
                    except Exception:
                        print(traceback.print_exc())
                if poc["end"]:
                    if "/" in poc["end"]:
                        print(self.url+poc["end"])
                    else:
                        print(self.url+"  "+poc["end"])
