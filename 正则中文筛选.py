#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/17 09:23
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 正则中文筛选.py
import re

str = '中文：123456aa哈哈哈bbcc收到噶'.decode('utf-8')

pattern = re.compile(u"[\u4e00-\u9fa5]+")

result = pattern.findall(str)

for item in result:
    print(item.encode('utf-8'))



