#coding=utf-8
import threading
import sys
sys.path.append("plugin")
from plugins.tomcat_special_plugin_ import tomcat_special_plugin_
from plugins.weblogic_special_plugin_ import weblogic_special_plugin_
from plugins.struts2_special_plugin_ import struts2_special_plugin_
from plugins.jboss_special_plugin_ import jboss_special_plugin_
from plugins.spring_special_plugin_ import spring_special_plugin_
from plugins.IIS_special_plugin_ import IIS_special_plugin_
from plugins.Nginx_special_plugin_ import Nginx_special_plugin_
def special_plugin_(arg,config):
    threads=[]
    threads.append(threading.Thread(tomcat_special_plugin_(arg,config)))
    threads.append(threading.Thread(weblogic_special_plugin_(arg,config)))
    threads.append(threading.Thread(jboss_special_plugin_(arg,config)))
    threads.append(threading.Thread(struts2_special_plugin_(arg, config)))
    threads.append(threading.Thread(spring_special_plugin_(arg,config)))
    threads.append(threading.Thread(IIS_special_plugin_(arg,config)))
    threads.append(threading.Thread(Nginx_special_plugin_(arg,config)))
    for thread in threads:
        try:
            thread.start()
        except Exception as e:
            print(e)
    for t in threads:
        t.join()

