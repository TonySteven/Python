#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py


# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:02
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : json.py


import json

# 加载文件
path = r"/Users/steven/PycharmProjects/Python/json/data/唐央央_life.json"
file = open(path, 'r', encoding='utf-8')
file1 = open(r"/Users/steven/PycharmProjects/Python/json/result/唐央央_life.txt", 'w')

# 解析数据
data = json.load(file)
records = data["RECORDS"]

for record in records:
    img_info = record["img_info"]
    img_info_lists = json.loads(img_info)

    for img_info_list in img_info_lists:
        url = img_info_list["url"]
        # 写入img_url
        file1.write(url)
        file1.write("\n")
