#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 6/10/22 16:24
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : 去除豆瓣图书目录页码.py


# 加载文件
book_path = r"/Users/steven/PycharmProjects/Python/json/book/book.txt"
f = open(book_path, 'r', encoding='utf-8')
file1 = open(r"/Users/steven/PycharmProjects/Python/json/book/new_book.txt", 'a')

lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
for line in lines:
    # print(line)
    r = line.split('　　', 1)
    file1.write(r[0])
    file1.write("\n")
