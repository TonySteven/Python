#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 10:40
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : UUID.py


a = input("请输入字符：")
b = []
for n in a :
   if "a"<= n <= "z":
      b.append(n.upper())
   # elif"A" <= n <= "Z" :
   #    b.append(n.lower())
   elif n == " " :
      b.append('_')
   else:
      b.append(n)
print("".join(b))
