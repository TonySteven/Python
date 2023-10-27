#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 3/22/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : analysis.py


# 输入参数 str 需要判断的字符串
# 返回值 True：该字符串为浮点数；False：该字符串不是浮点数。
def is_float_num(str):
    s = str.split('.')
    if len(s) > 2:
        return False
    else:
        for si in s:
            if not si.isdigit():
                return False
    return True


# 加载文件
work_path = r"/Users/steven/PycharmProjects/Python/json/book/good.txt"
file = open(work_path, 'r', encoding='utf-8')

# 解析数据
lines = file.readlines()

# 初始化总tax_amount
total_tax_amount = 0
# 读取全部内容 ，并以列表方式返回
for line in lines:
    # 打印第几行
    print(line)
    # 获取line里面goodsAmount获取到的值
    goodsAmount = line.split(",")[2].split("=")[1].strip()
    # 如果goodsAmount不是数字,则跳过
    if not IsFloatNum(goodsAmount):
        # 打印第三个是null的行
        print(line.split(",")[2])
        continue
    # 累加载文件里面的goodsAmount
    total_tax_amount += float(goodsAmount)

# 打印总tax_amount
print(total_tax_amount)
