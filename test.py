#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/10 17:01
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : test.py

import re

str = '{"commentid":"6422012514550734322","content":"一块两块","upcount":10,"isfriend":0,"isop":0,"isself":0,"timepoint":2242,"headurl":"http://thirdqq.qlogo.cn/g?b=oidb&k=rQaUcIcIesgB7xbNhfic7XQ&s=40","opername":"‭‭‭‭‭‭‭‭‭‭‭‭","content_style":""},{"commentid":"6422026331937272914","content":"第五人格的声音","upcount":13,"isfriend":0,"isop":0,"isself":0,"timepoint":2235,"headurl":"http://thirdqq.qlogo.cn/g?b=oidb&k=ZENquUSpDUVH1u1bHboc6g&s=40","opername":"冷心为后","content_style":""}'

pattern = re.compile(r'"content":".*?"')  # 查找数字
result1 = pattern.findall(str)
# result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
