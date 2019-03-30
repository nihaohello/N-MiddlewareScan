#coding=utf-8
import requests
import sys
import socket
def CVE_2017_12149(arg,config):
    try:
        port = 8080
        ip = socket.gethostbyname(arg.url.strip("http://").strip("https://"))
        url = 'http://{}:{}/invoker/JMXInvokerServlet'.format(ip, port)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
        r = requests.get(
            url, headers=headers, timeout=10, allow_redirects=False)
        if r.status_code == 200:
            if r.headers['content-type'].count('serialized') or r.headers['Content-Type'].count('serialized'):
                print('[ok] -> {}:{}'.format(ip, port))
            else:
                print("不存在 CVE_2017_12149 反序列化漏洞")
    except Exception:
        print("CVE_2017_12149 检测函数出错")
def jboss_special_plugin_(arg,config):
    CVE_2017_12149(arg,config)

