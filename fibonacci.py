#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/1/20 16:50
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : fibonacci.py
import sys


class Solution:
    def fibonacci(self, n):  # 生成器函数 - 斐波那契
        a, b, counter = 0, 1, 0
        while True:
            if (counter > n):
                return
            yield a
            a, b = b, a + b
            counter += 1


if __name__ == '__main__':
    s = Solution()
    f = s.fibonacci(10)  # f 是一个迭代器，由生成器返回生成
    while True:
        try:
            print(next(f), end=" ")
        except StopIteration:
            sys.exit()
