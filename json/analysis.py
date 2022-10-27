#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py

import json

nick_name = '凡漪'

work = '_w'
life = '_l'
# 加载文件
work_path = r"/Users/steven/PycharmProjects/Python/json/data/" + nick_name + work + ".json"
life_path = r"/Users/steven/PycharmProjects/Python/json/data/" + nick_name + life + ".json"
file = open(work_path, 'r', encoding='utf-8')
file1 = open(r"/Users/steven/PycharmProjects/Python/json/result/" + nick_name + ".txt", 'a')

# 解析数据
records = json.load(file)
# records = data["RECORDS"]

for record in records:
    img_info = record["img_info"]
    if img_info != '':
        img_info_lists = json.loads(img_info)

        for img_info_list in img_info_lists:
            url = img_info_list["url"]
            # 写入img_url
            file1.write(url)
            file1.write("\n")
