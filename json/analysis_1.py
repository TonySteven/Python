#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py

import json

nick_name = 'vid'

# 加载文件
work_path = r"/Users/steven/PycharmProjects/Python/json/data/" + nick_name + ".json"
file = open(work_path, 'r', encoding='utf-8')
file1 = open(r"/Users/steven/PycharmProjects/Python/json/result/" + nick_name + ".txt", 'a')

# 解析数据
data = json.load(file)
records = data["RECORDS"]

for record in records:
    json_data = record["JSON数据"]
    if json_data != '':
        json_data = json.loads(json_data)
        # 如果有videoContent,则保存,否则添加回车后继续循环.
        if 'videoContent' in json_data:
            video_Content = json_data["videoContent"]
            # 如果video_Content不为None并且有vid,则保存vid,否则跳过.
            if video_Content is not None and 'vid' in video_Content.keys():
                file1.write(video_Content["vid"])
                file1.write("\n")
            else:
                file1.write("\n")
                continue
        else:
            file1.write("\n")
            continue
    else:
        file1.write("\n")
