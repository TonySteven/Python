#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 11/25/20 15:42
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : lastRemaining.py

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        f = 0
        for i in range(2, n + 1):
            f = (m + f) % i
        return f


if __name__ == '__main__':
    n = 5
    m = 3
    s = Solution()
    result = s.lastRemaining(n,m)
    print(result)
