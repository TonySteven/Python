#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py

import json

from numpy import double

# 加载文件
work_path = r"/Users/steven/PycharmProjects/Python/json/book/response.json"
file = open(work_path, 'r', encoding='utf-8')

# 解析数据
records = json.load(file)
# records = data["data"]["rows"]

# 初始化总tax_amount
total_tax_amount = 0
# 打印records的数量
print(len(records))

for record in records:
    tax_amount = record["amount"]

    # 累加tax_amount
    total_tax_amount += double(tax_amount)

# 打印总tax_amount
print("总计金额: " + str(total_tax_amount))
