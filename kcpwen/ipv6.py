#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import os
import json
import sys

def login(username, password):
    if username == "" or password == "":
        return "请填写用户名密码"
    else:
        url = 'https://lgn6.bjut.edu.cn'
        d = {'DDDDD': username, 'upass': password,'v46s':'2','v6ip':'','f4serip':'172.21.75.57','0MKKey':''}
        r = requests.post(url, data=d)
        r.encoding='gbk'
        if u'登录成功窗' in r.text :
            return "ipv6登录成功"
        else : 
            return "ipv6登录失败"
def function(argv):
    if argv[1] == 'login':
        if len(argv) == 4:
            username = argv[2]
            password = argv[3]
            info = login(username, password)
            print(info)
        else :
            print("请输入网关账号密码,例如 python ipv6 login S201861847 123456")
        """
        try:
            with open("ipv6.json",'r') as load_f:
                load_dict = json.load(load_f)
                username = load_dict['username']
                password = load_dict['password']
                info = login(username, password)
                print(info)
        except IOError:
            print("配置文件读取失败")
        """
    elif argv[1] == 'logout':
        url = 'https://lgn6.bjut.edu.cn/F.htm'
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_cdce8cda34e84469b1c8015204129522=1547906203; __lnkrntdmcvrd=-1',
            'Host': 'lgn6.bjut.edu.cn',
            'Referer': 'https://lgn6.bjut.edu.cn/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        resp = requests.get(url=url, headers=headers,timeout=1)
        if resp.status_code==200:
            print("退出登录成功")
        else:
            print("退出登录失败")
if __name__ == "__main__":
    if len(sys.argv)==1:
        print("请输入参数\n1.login\n2.logout")
    else:
        function(sys.argv)
    
