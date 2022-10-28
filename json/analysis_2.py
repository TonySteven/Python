#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py

import json

import pandas as pd


# 把数据写入ExcelWriter方法
def write_data_into_excel(xlsPath: str, data_xls: dict):
    # mode=a 为追加模式
    # writer = pd.ExcelWriter(xlsPath, engine="openpyxl" , mode='a')

    writer = pd.ExcelWriter(xlsPath, engine="openpyxl")
    data_xls = pd.DataFrame(data_xls)
    data_xls.to_excel(writer, sheet_name="sheet1")
    # 如果省略该语句，则数据不会写入到上边创建的excel文件中
    writer.save()


# 设置文件名称
nick_name = 'course'

# 加载文件
work_path = r"//Users/stevenl/PycharmProjects/Python_new/json/data/" + nick_name + ".json"
file = open(work_path, 'r', encoding='utf-8')
file_xls_name = "/Users/stevenl/PycharmProjects/Python_new/json/result/" + nick_name + ".xlsx"

# 解析数据
data = json.load(file)
records = data["RECORDS"]

# 初始化写入Excel的字典数据
data_dict = {"课程名称": [], "vid": []}

for record in records:
    json_data = record["JSON数据"]
    if json_data != '':
        json_data = json.loads(json_data)
        # 如果有videoContent,则保存,否则添加回车后继续循环.
        if 'videoContent' in json_data:
            video_Content = json_data["videoContent"]
            # 如果video_Content不为None并且有vid,则保存vid,否则跳过.
            if video_Content is not None and 'vid' in video_Content.keys():
                course_name = record["课程名称"]

                # data_dict = dict.fromkeys(['课程名称', 'vid'])
                data_dict["课程名称"].append(course_name)
                data_dict["vid"].append(video_Content["vid"])
            else:
                continue
        else:
            continue

# 解析好数据,并写入Excel
write_data_into_excel(file_xls_name, data_dict)
