#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py

import json

# 加载文件
work_path = r"/Users/steven/PycharmProjects/Python/json/book/object.json"
file = open(work_path, 'r', encoding='utf-8')

# 解析数据
data = json.load(file)
records = data["detail"]

# 初始化总tax_amount
total_tax_amount = 0
# 打印records的数量
print(len(records))

for record in records:
    tax_amount = record["taxAmount"]
    # 判断tax_amount是否有超过2位小数的情况
    if len(str(tax_amount).split(".")[1]) > 2:
        print("tax_amount有超过2位小数的情况")
        print(tax_amount)

    # 累加tax_amount
    total_tax_amount += tax_amount

# 打印总tax_amount
print(total_tax_amount)
