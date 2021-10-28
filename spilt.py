#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 10/28/21 14:10
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : spilt.py
import json


def getSpilted(u):
    return json.dumps(u.split('、', -1))


if __name__ == '__main__':
    a = input("请输入要json格式化的字符：")
    print('\n')
    print(getSpilted(a))
