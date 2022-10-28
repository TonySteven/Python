#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/28/22 18:12
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 使用pandas把数据写入Excel文件.py

import pandas as pd


def writeDataIntoExcel(xlsPath: str, data_xls: dict):
    writer = pd.ExcelWriter(xlsPath)
    sheetNames = data_xls.keys()  # 获取所有sheet的名称
    # sheets是要写入的excel工作簿名称列表
    data_xls = pd.DataFrame(data_xls)
    for sheetName in sheetNames:
        data_xls.to_excel(writer, sheet_name=sheetName)
    # 保存writer中的数据至excel
    # 如果省略该语句，则数据不会写入到上边创建的excel文件中
    writer.save()


if __name__ == '__main__':
    data = {"name": ["lily", "ailcie"], "cost": [100, 20]}
    xls_path = "/Users/stevenl/PycharmProjects/Python_new/json/result/3.xls"
    writeDataIntoExcel(xls_path, data)
