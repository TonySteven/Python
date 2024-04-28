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

# 遍历并删除偶数行
for i in range(len(lines)):
    if i % 2 == 0:
        # 并\n前 新增分号
        file1.write(lines[i].strip() + ";" + "\n")
