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
import threading
import socket
def weblogic_special_plugin_(arg,config):
    port=7001
    ip=socket.gethostbyname(arg.url.strip("http://").strip("https://"))
    threads=[]
    threads.append(threading.Thread(CVE_2015_4852.run(ip,port)))
    threads.append(threading.Thread(CVE_2016_0638.run(ip,port,0)))
    threads.append(threading.Thread(CVE_2016_3510.run(ip,port,0)))
    threads.append(threading.Thread(CVE_2017_3248.run(ip,port,0)))
    threads.append(threading.Thread(CVE_2017_3506.run(ip,port)))
    threads.append(threading.Thread(CVE_2018_2893.run(ip,port,0)))
    threads.append(threading.Thread(CVE_2018_2628.run(ip,port,0)))
    threads.append(threading.Thread(managerURL200.run(ip,port)))
    threads.append(threading.Thread(uddi_ssrf.run(ip,port)))
    #print(arg.url)
    for thread in threads:
        thread.start()
    for j in threads:
        j.join()

    '''
        try:
        threads[0].strat()
    except Exception:
        print("CVE_2015_4852 脚本出错")
    try:
        threads[1].start()
    except Exception:
        print("CVE_2016_0638 脚本出错")
    try:
        threads[2].start()
    except Exception:
        print("CVE_2016_3510 脚本出错")
    try:
        threads[3].start()
    except Exception:
        print("CVE_2017_3248 脚本出错")
    try:
        threads[4].start()
    except Exception:
        print("CVE_2017_3506 脚本出错")
    try:
        threads[5].start()
    except Exception:
        print("CVE_2018_2893 脚本出错")
    try:
        threads[6].start()
    except Exception:
        print("CVE_2018_2628 脚本出错")
    try:
        threads[7].start()
    except Exception:
        print("managerURL200 脚本出错")
    try:
        threads[8].start()
    except Exception:
        print("uddi_ssrf 脚本出错")
    '''