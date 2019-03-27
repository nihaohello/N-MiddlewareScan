#coding=utf-8
import requests
import re
from concurrent.futures import ThreadPoolExecutor
import traceback
'''
s=requests.get(url="http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-9158")
s=s.text
s=re.findall("MISC:http.*",s)[0].rstrip("</a>").lstrip("MISC")
print(s)
'''
def requests_url(cve):
    try:
        url = "http://cve.mitre.org/cgi-bin/cvename.cgi?name=" + cve
        s = requests.get(url=url)
        s = s.text
        s = re.findall("MISC:http.*", s)[0].rstrip("</a>").lstrip("MISC:")
        print(s)
    except Exception:
        print(traceback.print_exc())


with open("temp2.txt") as f:
    for i in f.readlines():
        name = i.rstrip("\n")
        with ThreadPoolExecutor(40) as excetor:
            excetor.submit(requests_url(name))
f.close()



