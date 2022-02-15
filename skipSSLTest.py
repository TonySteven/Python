#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2/15/22 12:14
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : skipSSLTest.py


import requests

data = {'username': 'admin', 'password': 'admin'}
rs = requests.session()
r = rs.post('https://168.138.197.5:54321/login', data=data, verify=False).content
# print(str_name)
print(r.decode("utf-8"))
