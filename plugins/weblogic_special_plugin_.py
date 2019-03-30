#coding=utf-8
from plugins.weblogic_poc import CVE_2015_4852
from plugins.weblogic_poc import CVE_2016_0638
from plugins.weblogic_poc import CVE_2016_3510
from plugins.weblogic_poc import CVE_2017_3248
from plugins.weblogic_poc import CVE_2017_3506
from plugins.weblogic_poc import CVE_2018_2628
from plugins.weblogic_poc import CVE_2018_2893
from plugins.weblogic_poc import managerURL200
from plugins.weblogic_poc import uddi_ssrf
import socket
def weblogic_special_plugin_(arg,config):
    port=7001
    ip=socket.gethostbyname(arg.url.strip("http://").strip("https://"))
    #print(arg.url)
    try:
        CVE_2015_4852.run(ip,port)
    except Exception:
        print("CVE_2015_4852 脚本出错")
    try:
        CVE_2016_0638.run(ip,port,0)
    except Exception:
        print("CVE_2016_0638 脚本出错")
    try:
        CVE_2016_3510.run(ip,port,0)
    except Exception:
        print("CVE_2016_3510 脚本出错")
    try:
        CVE_2017_3248.run(ip,port,0)
    except Exception:
        print("CVE_2017_3248 脚本出错")
    try:
        CVE_2017_3506.run(ip,port)
    except Exception:
        print("CVE_2017_3506 脚本出错")
    try:
        CVE_2018_2893.run(ip,port,0)
    except Exception:
        print("CVE_2018_2893 脚本出错")
    try:
        CVE_2018_2628.run(ip,port,0)
    except Exception:
        print("CVE_2018_2628 脚本出错")
    try:
        managerURL200.run(ip,port)
    except Exception:
        print("managerURL200 脚本出错")
    try:
        uddi_ssrf.run(ip,port)
    except Exception:
        print("uddi_ssrf 脚本出错")