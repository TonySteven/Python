#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 6/10/22 16:24
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 左右新增单引号.py


# 加载文件
book_path = r"/Users/steven/PycharmProjects/Python/json/book/book.txt"
f = open(book_path, 'r', encoding='utf-8')
file1 = open(r"/Users/steven/PycharmProjects/Python/json/book/new_book.txt", 'a')

# 读取文件
lines = f.readlines()

for line in lines:
    # 前新增单引号 后面新增单引号加逗号。
    line = '"' + line.strip() + '"' + ","

    file1.write(line)
    file1.write("\n")
