#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/7 11:19
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : skipSSL.py

import requests;



rs = requests.session()
r = rs.get('https://www.baidu.com', verify=False).content

print (r)