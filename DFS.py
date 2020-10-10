#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-14 18:09
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : DFS.py

from collections import deque

F1 = open(r"/Users/steven/Downloads/maze.txt", "r")
List_row = F1.readlines()

map_array = []
for i in range(len(List_row)):
    column_list = List_row[i].strip().split("|")  # 每一行split后是一个列表
    map_array.append(column_list)  # 加入list_source

for i in range(len(map_array)):  # 行数
    for j in range(len(map_array[i])):  # 列数
        print(map_array[i][j])  # 输出每一项

# map_array = [[0, 0, 0, 0, 0, 0, 0, 0],
#              [0, 1, 1, 1, 1, 0, 1, 0],
#              [0, 0, 0, 0, 1, 0, 1, 0],
#              [0, 1, 0, 0, 0, 0, 1, 0],
#              [0, 1, 0, 1, 1, 0, 1, 0],
#              [0, 1, 0, 0, 0, 0, 1, 1],
#              [0, 1, 0, 0, 1, 0, 0, 0],
#              [0, 1, 1, 1, 1, 1, 1, 0]]

print("map_array====="+map_array)

# res = []
#
#
# class node:  # 定义位置结点类    
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# def dfs(x, y):
#     cur = node(x, y)
#     res.append(cur)
#     if x == 7 and y == 7:  # 走到出口
#         print(len(res))
#
#         for i in range(len(res)):
#             print(" (" + str(res[i].x) + "," + str(res[i].y) + ")", end="") #end干掉,输入换行
#         return True
#     if x == 8 or x == -1 or y == 8 or y == -1 or map_array[x][y] == 1:  # 超出范围或遇到墙
#         return False
#     map_array[x][y] = 1
#     if dfs(x + 1, y):  # 向右走
#         return
#     if dfs(x - 1, y):  # 向左走
#         return
#     if dfs(x, y + 1):  # 向下走
#         return
#     if dfs(x, y - 1):  # 向上走
#         return
#     map_array[x][y] = 0
#     res.pop()
#
#
# dfs(0, 0)
