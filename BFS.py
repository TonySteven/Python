#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-10-14 18:00
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : BFS.py


from collections import deque

x = deque([])  # 横坐标
y = deque([])  # 纵坐标
s = deque([])  # 代表步长

a = [[0 for col in range(8)] for row in range(8)]  # 初始化迷宫
b = [[0 for col in range(8)] for row in range(8)]  # 初始化标记数组

next_step = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 迷宫的四种走法

start_x = 0  # 迷宫的起点
start_y = 0
end_x = 7  # 迷宫的终点
end_y = 7
map_array = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 1, 1, 1, 0, 1, 0],
             [0, 0, 0, 0, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 1, 0],
             [0, 1, 0, 1, 1, 0, 1, 0],
             [0, 1, 0, 0, 0, 0, 1, 1],
             [0, 1, 0, 0, 1, 0, 0, 0],
             [0, 1, 1, 1, 1, 1, 1, 0]]

for i in range(len(map_array)):
    for j in range(len(map_array)):
        a[i][j] = map_array[i][j]  # 将迷宫填入a中

head = 0  # 队列的头和尾
tail = 0

x.append(start_x)
y.append(start_y)
s.append(0)
tail += 1

b[start_x][start_y] = 1  # 将起点设为1，代表已经走过

flag = 0  # 表示是否已经走到终点，1表示走到了，0表示没有

while head < tail:
    for i in range(len(next_step)):
        next_x = x[head] + next_step[i][0]
        next_y = y[head] + next_step[i][1]
        if next_x < 0 or next_y < 0 or next_x > 7 or next_y > 7:  # 走出边界
            continue
        if a[next_x][next_y] == 0 and b[next_x][next_y] == 0:  # 下一步不是墙而且没有走过
            b[next_x][next_y] = 1
            x.append(next_x)
            y.append(next_y)
            s.append(s[head] + 1)  # x,y分别增加到队列，步长加一
            tail += 1
        if next_x == end_x and next_y == end_y:
            flag = 1
            break
    if flag == 1:
        break
    head += 1  # 继续对后面的点进行扩展

print('The process of x_queue:{}'.format(x))  # 输出x走过的路径
print('The process of y_queue:{}'.format(y))  # 输出y走过的路径