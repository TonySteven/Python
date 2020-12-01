#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/1/20 23:09
# @Author  : StevenL
# @Email   : stevenl365404@gmail.com
# @File    : sumNums.py

class Solution:
    def sumNums(self, n: int) -> int:
        return sum(range(n+1))


if __name__ == '__main__':
    n = 3
    s = Solution()
    result = s.sumNums(n=n)
    print(result)

