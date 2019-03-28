#coding=utf-8
import sys
import requests
import os
import json
import traceback
sys.path.append("plugins")
import plugins
current_file=os.path.dirname(os.path.abspath(__file__))
from user_agent import get_user_agent
class plugins(object):
    def __init__(self,url,options):
        self.url=url
        self.options=options
    def run(self):
        files=os.listdir(current_file)
        for file in files:
            if "_plugin.py" in file:
                module=file.rstrip(".py")
                pocs=__import__(module).pocs
                self.check(pocs)
    def check(self,pocs):
        for poc in pocs:
            for url in poc["url"]:
                try:
                    success_num = 0
                    url = self.url + url
                    if poc["requests_option"] == "GET":
                        if not poc["params"]:
                            poc["params"].append("seize")
                        for params in poc["params"]:
                            success_num=0
                            try:
                                headers = {'User-Agent': get_user_agent()}
                                s = requests.get(url=url, params=params, headers=headers)
                                for flag in poc["flag"]:
                                    if flag in s.text:
                                        success_num = success_num + 1
                                if success_num > 0:
                                    print(poc["success"]+" , url: "+url)
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
                                            success_num=0
                                            headers = {'User-Agent': get_user_agent()}
                                            s = requests.post(url=url, data=data, headers=headers)
                                            for flag in poc["flag"]:
                                                if flag in s.text:
                                                    success_num = success_num + 1
                                            if success_num > 0:
                                                print("success url:"+utl+" "+poc["success"] + ",username:%s password:%s" % (username, password))
                            except Exception:
                                print(traceback.print_exc())
                            else:
                                try:
                                    for data in poc["data"]:
                                        success_num=0
                                        headers = {'User-Agent': get_user_agent()}
                                        s = requests.post(url=url, data=data, headers=headers)
                                        for flag in poc["flag"]:
                                            if flag in s.text:
                                                success_num = success_num + 1
                                        if success_num > 0:
                                            print("success url:" + utl + " " + poc["success"])
                                except Exception:
                                    print(traceback.print_exc())
                except Exception:
                    print(traceback.print_exc())
            print(poc["end"])
